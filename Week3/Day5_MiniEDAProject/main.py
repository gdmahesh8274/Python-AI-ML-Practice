# Week 3 - Day 5 - Mini EDA Project
# Perform exploratory data analysis on a sample CSV dataset.

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

folder = Path(__file__).parent
df = pd.read_csv(folder / "students.csv")

print("First Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean().round(2))

# Chart 1: Marks by student
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(folder / "student_marks.png")
plt.close()

# Chart 2: Study hours vs marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.savefig(folder / "study_hours_vs_marks.png")
plt.close()

# Chart 3: Marks distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(folder / "marks_distribution.png")
plt.close()

print("\nKey Findings:")
print("1. Sara has the highest marks.")
print("2. Alex has the lowest marks.")
print("3. Higher study hours are associated with higher marks in this sample.")
print("4. IT has the highest average marks in this sample.")
print("5. No missing values are present in the dataset.")
print("\nCharts saved in the project folder.")
