# Week 2 - Day 4 - GroupBy Basics
# Use groupby to calculate counts and averages by category.

import pandas as pd

data = {
    "Name": ["Mahesh", "John", "Sara", "David", "Emma", "Sophia"],
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR"],
    "Marks": [85, 78, 92, 80, 88, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nStudent Count by Department:")
print(df.groupby("Department")["Name"].count())

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())
