# Week 6 - Day 4 - Real Outlier Handling
# Detect and cap extreme values in a sample dataset.

import pandas as pd

df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Study_Hours": [2, 3, 4, 5, 3, 4, 6, 40]
})

q1 = df["Study_Hours"].quantile(0.25)
q3 = df["Study_Hours"].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

print("Original data:")
print(df)
print("\nOutlier rows:")
print(df[(df["Study_Hours"] < lower_limit) | (df["Study_Hours"] > upper_limit)])

# Cap extreme values instead of removing the students.
df["Study_Hours_Clean"] = df["Study_Hours"].clip(lower_limit, upper_limit)

print("\nData after capping:")
print(df)
print("\nAlways investigate whether an outlier is a data error before changing it.")
