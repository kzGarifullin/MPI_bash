
from mpi4py import MPI
import numpy
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact
comm = MPI.COMM_WORLD#коммуникатор глобальный
size = comm.Get_size()#общее кол-во процессов в данном коммуникаторе
rank = comm.Get_rank()#номер процесса вызвавшего данную функцию 0 1 2 3 - нумерация четырех процессов
'''
N = 10000
    print("Calculated pi is ", pi)
    print("size:", size)
'''
p = p_var
n = n_var
N = n
#N = 150#число членов в ряде
s = 0.0
start = MPI.Wtime()

for i in range(rank, N, size):
    s += 1.0/factorial(i)
myexp = s
exp = comm.reduce(myexp, op=MPI.SUM, root=0)
end = MPI.Wtime()
if rank == 0:
    print("Calculation time is ", end - start)
    print("Calculated e is ", exp)
    print("size:", size)

