# Title:

Implementation of a ribbon algorithm for matrix multiplication

# Objective:

Using MPI technology in python, perform two matrices multiplication using a ribbon scheme, compare with the execution of sequential 
(non-parallelized) code. And also to plot the dependence of running time, acceleration and efficiency depending on the number of 
processors p and  matrix size n.

-----------------
Matrix A will be filled with random numbers from 1 to 100, matrix B will be taken without loss of generality by matrix A.
Parallelization will be in the following way: the processor with zero rank will distribute matrix A among the remaining processors. That is, one processor will calculate matrix elements while running the calculation on two processors. Let's call A_part the part of matrix A distributed to the given processor.

-----------------
Script review:

0. Matrix_generate.py - creates a random matrix of desired size

1. Matrix_multiplication.py - calculates the time and the multiplication itself

2. run_all.sh - launches calculation for different numbers of processors and partitions

3. read_data.py - processing data and writing them into the document

Processing result as follows: 1 column - number of processors, 2 - number of matrix rows, 3 - time

-----------------

n_10000_p_11.out, n_10000_p_5.out, n_1000_p_14.out, n_1000_p_8.out, n_100_p_2.out - the results of the matrix multiplication code, which was run on p processors using a matrix of size n

mult.out - the result of calculating the time of all tasks in the form of a table
