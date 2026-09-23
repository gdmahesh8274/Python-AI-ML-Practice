# Week 3 - Day 2 - Scatter Plot
# Plot two numerical columns and observe their relationship.

import matplotlib.pyplot as plt

hours_studied = [1, 2, 3, 4, 5, 6, 7]
marks = [50, 55, 65, 70, 78, 85, 92]

plt.scatter(hours_studied, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.grid(True)

plt.show()

# Observation:
# Marks generally increase as study hours increase.
