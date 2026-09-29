# Week 4 - Day 1 - Feature and Target Identification
# Identify independent and dependent variables in a dataset.

import pandas as pd

data = {
    "Hours_Studied": [2, 4, 6, 8],
    "Attendance": [65, 75, 85, 95],
    "Marks": [55, 70, 85, 95]
}

df = pd.DataFrame(data)

# Independent variables (features)
X = df[["Hours_Studied", "Attendance"]]

# Dependent variable (target)
y = df["Marks"]

print("Features (X):")
print(X)

print("\nTarget (y):")
print(y)
