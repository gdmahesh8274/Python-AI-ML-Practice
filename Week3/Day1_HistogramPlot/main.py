# Week 3 - Day 1 - Histogram Plot
# Create a histogram using sample numerical data and experiment with bins.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = np.random.randint(50, 101, size=50)

plt.hist(data, bins=10, edgecolor="black")

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
