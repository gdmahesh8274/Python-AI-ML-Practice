# Week 2 - Day 3 - Column Selection
# Select single and multiple columns and filter rows using conditions.

import pandas as pd

data = {
    "Name": ["Mahesh", "John", "Sara", "David", "Emma"],
    "Age": [25, 24, 26, 27, 23],
    "Marks": [85, 78, 92, 80, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Select one column
print("\nName Column:")
print(df["Name"])

# Select multiple columns
print("\nName and Marks Columns:")
print(df[["Name", "Marks"]])

# Filter rows using a condition
print("\nStudents with marks greater than or equal to 85:")
print(df[df["Marks"] >= 85])

# Filter using two conditions
print("\nStudents age 25 or older with marks 80 or above:")
print(df[(df["Age"] >= 25) & (df["Marks"] >= 80)])
