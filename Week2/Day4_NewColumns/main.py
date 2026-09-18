# Week 2 - Day 4 - New Column Creation
# Create new columns using calculations from existing columns.

import pandas as pd

data = {
    "Name": ["Mahesh", "John", "Sara", "David"],
    "Math": [85, 70, 92, 80],
    "Science": [90, 75, 88, 82],
    "English": [80, 78, 94, 76]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Percentage"] = df["Total"] / 3

print("Student Results:")
print(df)
