# Week 2 - Day 4 - Sorting and Renaming
# Rename columns and sort records by values.

import pandas as pd

data = {
    "Student": ["Mahesh", "John", "Sara", "David", "Emma"],
    "Score": [85, 78, 92, 80, 88],
    "Age": [25, 24, 26, 27, 23]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df = df.rename(columns={"Student": "Name", "Score": "Marks"})
print("\nAfter Renaming Columns:")
print(df)

sorted_df = df.sort_values(by="Marks", ascending=False)
print("\nSorted by Marks:")
print(sorted_df)

sorted_multiple = df.sort_values(by=["Age", "Marks"])
print("\nSorted by Age and Marks:")
print(sorted_multiple)
