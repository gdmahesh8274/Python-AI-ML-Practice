# Week 2 - Day 1 - Array Indexing and Slicing
# Practice accessing elements, rows, columns, and slices.

import numpy as np

array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Array:")
print(array)

# Access one element
print("\nFirst element:", array[0, 0])
print("Center element:", array[1, 1])

# Access rows
print("\nFirst row:", array[0])
print("Last row:", array[2])

# Access columns
print("\nFirst column:", array[:, 0])
print("Second column:", array[:, 1])

# Slice rows and columns
print("\nFirst two rows:")
print(array[0:2])

print("\nFirst two columns:")
print(array[:, 0:2])
