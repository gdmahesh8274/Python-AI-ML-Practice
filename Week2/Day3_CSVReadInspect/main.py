# Week 2 - Day 3 - CSV Read and Inspect
# Load a CSV file and inspect it with head, tail, info, and describe.

import pandas as pd

# Read the CSV file
df = pd.read_csv("students.csv")

print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataFrame Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
