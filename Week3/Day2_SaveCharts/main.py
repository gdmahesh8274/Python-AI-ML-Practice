# Week 3 - Day 2 - Save Charts to File
# Save generated charts as image files inside this project folder.

import matplotlib.pyplot as plt

subjects = ["Python", "NumPy", "Pandas", "Matplotlib"]
scores = [85, 80, 88, 75]

# Save a bar chart.
plt.figure(figsize=(8, 5))
plt.bar(subjects, scores)
plt.title("Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.tight_layout()
plt.savefig("subject_scores.png")
plt.close()

# Save a line chart.
days = [1, 2, 3, 4, 5]
marks = [65, 72, 78, 84, 90]

plt.figure(figsize=(8, 5))
plt.plot(days, marks, marker="o")
plt.title("Marks Progress")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.savefig("marks_progress.png")
plt.close()

print("Charts saved as subject_scores.png and marks_progress.png")
