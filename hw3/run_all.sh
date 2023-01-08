
for p in $(seq 5 6)
do
        for n in 20000
        #for n in 10 100 1000 10000
        do
                cp matrix_multiplication.py n-${n}-p-${p}.py
                sed -i -e "s/p_var/${p}/g" -e "s/n_var/${n}/g" n-${n}-p-${p}.py
                sbatch -J k.garif  -N 1 -o "n_${n}_p_${p}.out" --ntasks-per-node=$p --wrap="mpirun -np ${p} python n-${n}-p-${p}.py" --exclusive
        done
done
