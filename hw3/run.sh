#!/bin/bash
#SBATCH -N 1 --ntasks-per-node=8 --job-name mpi_python
#SBATCH --comment "MPI python"
#SBATCH -e errors.log

mpirun -np 1 python matrix_generate.py
