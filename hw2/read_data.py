
for p in range(1,17):
    for n in [1000, 5000, 10000, 50000, 100000, 500000, 1000000]:
        name = "n_" + str(n) + "_p_" + str(p) +".out"
        f = open(name)
        count = 0
        for line in f:
            count +=1
            if(count==1):
                a=line.split()
                print(p, n, float(a[3]))
            else:
                continue
