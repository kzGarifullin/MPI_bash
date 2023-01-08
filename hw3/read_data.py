
for p in range(2,17):
    for n in [10,100, 1000, 10000, 20000]:
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
