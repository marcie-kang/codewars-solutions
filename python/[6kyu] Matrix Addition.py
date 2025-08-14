"""
Write a function that accepts two square matrices (N x N two dimensional arrays), and return the sum of the two. Both matrices being passed into the function will be of size N x N (square), containing only integers.

How to sum two matrices:

Take each cell [n][m] from the first matrix, and add it with the same [n][m] cell from the second matrix. This will be cell [n][m] of the solution matrix. (Except for C where solution matrix will be a 1d pseudo-multidimensional array).
"""

def matrix_addition(a, b):
    outer = []

    for i in range(len(a)):
        inner = []

        for j in range(len(a[i])):
            sum = a[i][j] + b[i][j]
            inner.append(sum)

        outer.append(inner)

    return outer
