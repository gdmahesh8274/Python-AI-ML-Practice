# Week 2 - Day 3 - Pandas Series Practice
# Create Pandas Series and practice indexing, filtering, and value access.

import pandas as pd

marks = pd.Series([85, 72, 90, 68, 88], index=["Mahesh", "John", "Sara", "David", "Emma"])

print("Student Marks:")
print(marks)

# Access values using labels
print("\nMahesh's mark:", marks["Mahesh"])
print("Sara's mark:", marks["Sara"])

# Access a value using position
print("\nFirst value:", marks.iloc[0])

# Filter the Series
print("\nMarks greater than or equal to 80:")
print(marks[marks >= 80])
