# Week 3 - Day 1 - Bar Chart
# Create a bar chart using categories and values.

import matplotlib.pyplot as plt

subjects = ["Python", "NumPy", "Pandas", "Matplotlib"]
scores = [85, 80, 88, 75]

plt.bar(subjects, scores)

plt.title("Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")

plt.show()
