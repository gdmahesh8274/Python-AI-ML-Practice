# Week 2 - Day 2 - Matrix Operations
# Create two matrices and perform addition and multiplication using NumPy.

import numpy as np

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Matrix multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)
