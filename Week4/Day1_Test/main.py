# Week 4 - Day 1 - Test: Visualization and EDA
# Inspect data, create charts, and summarize findings.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Mahesh", "John", "Sara", "David", "Emma"],
    "Hours_Studied": [5, 3, 7, 4, 6],
    "Marks": [85, 70, 95, 78, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nSummary:")
print(df.describe())

plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

print("\nFinding:")
print("Students who studied more hours generally scored higher in this sample.")
