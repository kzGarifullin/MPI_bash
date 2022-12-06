
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD#коммуникатор глобальный
size = comm.Get_size()#общее кол-во процессов в данном коммуникаторе
rank = comm.Get_rank()#номер процесса вызвавшего данную функцию 0 1 2 3 - нумерация четырех процессов

p = p_var
n = n_var
#N = p * n
N = n
#N = 10000
h = 1.0 / N
s = 0.0
start = MPI.Wtime()

for i in range(rank, N, size):
    x = h * (i + 0.5)
    s += 4.0 / (1.0 + x**2)
mypi = h * s
pi = comm.reduce(mypi, op=MPI.SUM, root=0)
end = MPI.Wtime()
if rank == 0:
    print("Calculation time is ", end - start)
    print("Calculated pi is ", pi)
    print("p: ", p)
    print("n: ", n)
