# Title:

Implementation of a ribbon algorithm for matrix multiplication

# Objective:

Using MPI technology in python, perform two matrices multiplication using a ribbon scheme, compare with the execution of sequential 
(non-parallelized) code. And also to plot the dependence of running time, acceleration and efficiency depending on the number of processors p and 
matrix size n.
-----------------
Script review:

0)matrix_generate.py - creates a random matrix of desired size

1)matrix_multiplication.py - calculates the time and the multiplication itself

2) run_all.sh - launches calculation for different numbers of processors and partitions

3) read_data.py - processing data and writing them into the document

Processing result as follows: 1 column - number of processors, 2 - number of matrix rows, 3 - time

Translated with www.DeepL.com/Translator (free version)
