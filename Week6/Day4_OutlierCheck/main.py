# Week 6 - Day 4 - Outlier Check
# Use the IQR method to detect unusual values.

import pandas as pd

df = pd.DataFrame({"Marks": [65, 70, 72, 75, 78, 80, 82, 85, 90, 150]})

q1 = df["Marks"].quantile(0.25)
q3 = df["Marks"].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = df[(df["Marks"] < lower_limit) | (df["Marks"] > upper_limit)]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)
print("\nOutliers:")
print(outliers)
