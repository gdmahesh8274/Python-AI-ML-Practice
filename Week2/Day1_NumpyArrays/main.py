# Week 2 - Day 1 - NumPy Array Creation
# Create 1D and 2D arrays and inspect shape, size, and dimensions.

import numpy as np

# Create a 1D array
array_1d = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(array_1d)
print("Shape:", array_1d.shape)
print("Size:", array_1d.size)
print("Dimensions:", array_1d.ndim)

# Create a 2D array
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(array_2d)
print("Shape:", array_2d.shape)
print("Size:", array_2d.size)
print("Dimensions:", array_2d.ndim)
