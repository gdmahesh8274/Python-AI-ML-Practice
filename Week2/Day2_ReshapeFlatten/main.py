# Week 2 - Day 2 - Reshape and Flatten
# Use reshape and flatten and compare the outputs.

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(array)
print("Original Shape:", array.shape)

# Reshape 1D array into a 2D array
reshaped_array = array.reshape(2, 3)
print("\nReshaped Array:")
print(reshaped_array)
print("Reshaped Shape:", reshaped_array.shape)

# Flatten the 2D array back into a 1D array
flattened_array = reshaped_array.flatten()
print("\nFlattened Array:")
print(flattened_array)
print("Flattened Shape:", flattened_array.shape)
