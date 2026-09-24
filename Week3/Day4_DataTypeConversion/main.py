# Week 3 - Day 4 - Data Type Conversion
# Convert strings to numeric values, parse dates, and adjust category types.

import pandas as pd

data = {
    "Name": ["Mahesh", "John", "Sara"],
    "Marks": ["85", "78", "92"],
    "JoinDate": ["2026-09-01", "2026-09-05", "2026-09-10"],
    "Department": ["IT", "HR", "IT"]
}

df = pd.DataFrame(data)

print("Before Conversion:")
print(df.dtypes)

df["Marks"] = pd.to_numeric(df["Marks"])
df["JoinDate"] = pd.to_datetime(df["JoinDate"])
df["Department"] = df["Department"].astype("category")

print("\nAfter Conversion:")
print(df.dtypes)

print("\nData:")
print(df)
