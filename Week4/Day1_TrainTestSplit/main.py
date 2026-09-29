# Week 4 - Day 1 - Train-Test Split
# Separate features and target and apply train_test_split.

import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "Marks": [50, 55, 62, 68, 75, 82, 88, 95]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied", "Attendance"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("Training Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)
