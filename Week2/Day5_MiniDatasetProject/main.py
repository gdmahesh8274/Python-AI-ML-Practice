# Week 2 - Day 5 - Mini Dataset Project
# Clean and analyze a small student marks dataset.

import pandas as pd

df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing marks with the column average
df["Science"] = df["Science"].fillna(df["Science"].mean())

# Create total and average columns
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\nCleaned Dataset:")
print(df)

print("\nOverall Average Marks:")
print(round(df["Average"].mean(), 2))

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Average"].mean().round(2))

print("\nHighest Average Student:")
print(df.loc[df["Average"].idxmax(), ["Name", "Average"]])
