# Week 3 - Day 1 - Matplotlib Basics
# Create a simple line chart with title and axis labels.

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [70, 75, 80, 78, 85]

plt.plot(days, marks, marker="o")

plt.title("Student Marks Progress")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.grid(True)

plt.show()
