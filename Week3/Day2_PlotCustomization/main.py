# Week 3 - Day 2 - Plot Customization
# Improve readability with legends, gridlines, markers, and figure size.

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
python_scores = [60, 68, 75, 82, 90]
pandas_scores = [55, 65, 72, 80, 86]

plt.figure(figsize=(8, 5))

plt.plot(days, python_scores, marker="o", label="Python")
plt.plot(days, pandas_scores, marker="s", label="Pandas")

plt.title("Learning Progress")
plt.xlabel("Day")
plt.ylabel("Score")
plt.legend()
plt.grid(True)

plt.show()
