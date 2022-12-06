
for p in $(seq 1 16)
do
        for n in 1000 5000 10000 50000 100000 500000 1000000
        do
                cp PI_mpi.py n-${n}-p-${p}.py
                sed -i -e "s/p_var/${p}/g" -e "s/n_var/${n}/g" n-${n}-p-${p}.py
                sbatch -J k.garif  -N 1 -o "n_${n}_p_${p}.out" --ntasks-per-node=$p --wrap="mpirun -np ${p} python n-${n}-p-${p}.py" --exclusive
        done
done
