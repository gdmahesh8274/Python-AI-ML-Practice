# Week 2 - Day 2 - Basic Statistics
# Calculate mean, median, and standard deviation using NumPy.

import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Numbers:", numbers)

# NumPy calculations
mean = np.mean(numbers)
median = np.median(numbers)
standard_deviation = np.std(numbers)

print("\nUsing NumPy:")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", standard_deviation)

# Manual mean calculation for comparison
manual_mean = sum(numbers) / len(numbers)
print("\nManual Mean:", manual_mean)
