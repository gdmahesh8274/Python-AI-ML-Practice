# Week 3 - Day 2 - Multiple Plot Practice
# Create separate charts and understand the purpose of each chart.

import matplotlib.pyplot as plt

subjects = ["Python", "NumPy", "Pandas", "Matplotlib"]
scores = [85, 80, 88, 75]

# Line chart - useful for showing changes or trends.
plt.figure()
plt.plot(subjects, scores, marker="o")
plt.title("Line Chart - Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()

# Bar chart - useful for comparing categories.
plt.figure()
plt.bar(subjects, scores)
plt.title("Bar Chart - Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()

# Histogram - useful for showing the distribution of numerical data.
marks = [55, 60, 62, 68, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95]

plt.figure()
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Histogram - Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
