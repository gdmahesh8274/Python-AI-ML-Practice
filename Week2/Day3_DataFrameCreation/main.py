# Week 2 - Day 3 - DataFrame Creation
# Create DataFrames from a dictionary and a list, then inspect rows and columns.

import pandas as pd

# DataFrame from a dictionary
data = {
    "Name": ["Mahesh", "John", "Sara", "Emma"],
    "Age": [25, 24, 26, 23],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)

print("DataFrame from Dictionary:")
print(df)

print("\nFirst two rows:")
print(df.head(2))

print("\nColumns:")
print(df.columns)

# DataFrame from a list
students = [
    ["David", 27, 80],
    ["Sophia", 22, 91]
]

df_list = pd.DataFrame(students, columns=["Name", "Age", "Marks"])

print("\nDataFrame from List:")
print(df_list)
