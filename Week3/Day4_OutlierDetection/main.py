# Week 3 - Day 4 - Outlier Detection Basics
# Detect outliers using a box plot and the IQR method.

import pandas as pd
import matplotlib.pyplot as plt

data = {"Marks": [65, 70, 72, 75, 78, 80, 82, 85, 88, 90, 150]}
df = pd.DataFrame(data)

q1 = df["Marks"].quantile(0.25)
q3 = df["Marks"].quantile(0.75)
iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = df[(df["Marks"] < lower_limit) | (df["Marks"] > upper_limit)]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("\nOutliers:")
print(outliers)

plt.boxplot(df["Marks"])
plt.title("Marks Outlier Detection")
plt.ylabel("Marks")
plt.show()
