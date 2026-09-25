# Week 3 - Day 4 - Data Cleaning Practice
# Identify and remove duplicate rows and standardize column formats.

import pandas as pd

data = {
    "Name": ["Mahesh", "John", "Mahesh", "Sara"],
    "City": ["chicago", "NEW YORK", "chicago", "dallas"],
    "Marks": [85, 78, 85, 92]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nDuplicate Rows:")
print(df.duplicated())

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize text column formats
df["Name"] = df["Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

print("\nCleaned Data:")
print(df)
