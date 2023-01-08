import random
N=30000

f = open(f'A{N}.dat', 'w')
for i in range(N*N):
    index = int(random.uniform(0, 100))
    f.write(str(index) + '\n')
f.close()
f2 = open(f'in{N}.dat', 'w')
f2.write(str(N) + '\n')
f2.write(str(N) + '\n')
f2.close()
