# Week 2 - Day 4 - Missing Values Basics
# Identify, fill, and drop missing values using Pandas.

import pandas as pd
import numpy as np

data = {
    "Name": ["Mahesh", "John", "Sara", "David", "Emma"],
    "Age": [25, np.nan, 26, 27, 23],
    "Marks": [85, 78, np.nan, 80, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

filled_df = df.fillna({"Age": df["Age"].mean(), "Marks": df["Marks"].mean()})
print("\nAfter Filling Missing Values:")
print(filled_df)

dropped_df = df.dropna()
print("\nAfter Dropping Missing Values:")
print(dropped_df)
