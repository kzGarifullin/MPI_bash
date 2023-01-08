from mpi4py import MPI
from numpy import empty, array, int32, float64, ones, dot
import numpy as np
NPASTE = n_var
p = p_var
def transform(a):
    b = a.copy()
    b[0]=a[0]
    for i in range(1,len(a)-1):
        b[i]=(a[i-len(a)+1])
    b[-1]=a[1]
    return b
comm = MPI.COMM_WORLD
numprocs = comm.Get_size()
rank = comm.Get_rank()
#start = MPI.Wtime()
if rank == 0 :
    f1 = open(f'in{NPASTE}.dat', 'r')
    N = array(int32(f1.readline()))
    M = array(int32(f1.readline()))
    f1.close()
else :
    N = array(0, dtype=int32)

comm.Bcast([N, 1, MPI.INT], root=0)

if rank == 0 :
    ave, res = divmod(M, numprocs-1)
    rcounts = empty(numprocs, dtype=int32)
    displs = empty(numprocs, dtype=int32)
    rcounts[0] = 0; displs[0] = 0
    for k in range(1, numprocs) : 
        if k < 1 + res :
            rcounts[k] = ave + 1
        else :
            rcounts[k] = ave
        displs[k] = displs[k-1] + rcounts[k-1]
else :
    rcounts = None; displs = None

M_part = array(0, dtype=int32)

comm.Scatterv([rcounts, ones(numprocs), array(range(numprocs)), MPI.INT], 
              [M_part, 1, MPI.INT], root=0)  # comm.Scatter([rcounts, 1, MPI.INT], [M_part, 1, MPI.INT], root=0) 

A_part = empty((M_part, N), dtype=float64)  
if rank == 0 :
    f2 = open(f'A{NPASTE}.dat', 'r')
    A = empty((M,N), dtype=float64)
    for j in range(M) :
        for i in range(N) :
            A[j,i] = float64(f2.readline())
    f2.close()
    
if rank == 0 :
    B = empty((M,N), dtype=float64)
    for j in range(M):
        for i in range(N):
            B[j,i]=A[i,j]

if rank ==0 :
    comm.Scatterv([A, rcounts*N, displs*N, MPI.DOUBLE], 
                  [A_part, M_part*N, MPI.DOUBLE], root=0)   
else :
    comm.Scatterv([None, None, None, None], 
                  [A_part, M_part*N, MPI.DOUBLE], root=0)    
if rank == 0 :
    b = empty((M,N), dtype=float64)
else:
    b = None
#B-its A transported matrix
#reading and transposing B
start = MPI.Wtime()
for k in range(numprocs-1):
    #B_part = empty((M_part, N), dtype=float64)
    #M_part = array(0, dtype=int32)
    r = numprocs-1
    if k == 0:
        B_part = empty((M_part, N), dtype=float64)
        if rank == 0:    
            comm.Scatterv([B, rcounts*N, displs*N, MPI.DOUBLE], [B_part, M_part*N, MPI.DOUBLE], root=0)
        else :
            comm.Scatterv([None, None, None, None], [B_part, M_part*N, MPI.DOUBLE], root=0)
    else:
        if rank == 0:
            #print(rcounts)
            #print(displs)
            rcounts= transform(rcounts)
            displs = transform(displs)        
        else :    
            rcounts = None; displs = None
        #print(rcounts)
        M_part = array(0, dtype=int32)
        
        comm.Scatterv([rcounts, ones(numprocs), array(range(numprocs)), MPI.INT],[M_part, 1, MPI.INT], root=0)
        #print("M_part: ",M_part)
        B_part = empty((M_part, N), dtype=float64)
        if rank == 0:
            
            #print(M_part)
            comm.Scatterv([B, rcounts*N, displs*N, MPI.DOUBLE], [B_part, M_part*N, MPI.DOUBLE], root=0)
            #print(M_part)
        else :
            comm.Scatterv([None, None, None, None], [B_part, M_part*N, MPI.DOUBLE], root=0)

    #print("rank: ", rank," B_part:", B_part)    
    #b_part = dot(A_part, B_part)
    b_part = dot(A_part, np.array(B_part).T)
    #print("rank: ", rank," A_part:", A_part)
    #print("rank: ", rank," b_part:", b_part)

    comm.Gatherv([b_part, M_part, MPI.DOUBLE], [b, rcounts, displs, MPI.DOUBLE], root=0)
    #print(b)
end = MPI.Wtime()    
if rank == 0: 	
# Сохраняем результат вычислений в файл
    f4 = open(f'Results{NPASTE}.dat', 'w')
    
    for j in range(M) :
        f4.write(str(b[j]))
        f4.write('\n')
    f4.close()
    print("Calculation time is: ", end - start)
    print("------")
    print("p: ", p)
    print("N: ", NPASTE)
    print(b)
