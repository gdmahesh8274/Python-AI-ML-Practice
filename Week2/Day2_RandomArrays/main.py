# Week 2 - Day 2 - Random Number Arrays
# Generate random integers and floats and inspect their values and ranges.

import numpy as np

# Random integers from 1 to 100
random_integers = np.random.randint(1, 101, size=10)

print("Random Integers:")
print(random_integers)
print("Minimum:", random_integers.min())
print("Maximum:", random_integers.max())

# Random floats between 0 and 1
random_floats = np.random.random(5)

print("\nRandom Floats:")
print(random_floats)
print("Minimum:", random_floats.min())
print("Maximum:", random_floats.max())
