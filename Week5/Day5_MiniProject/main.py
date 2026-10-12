# Week 5 - Day 5 - Student Performance Mini Project
# Predict whether a student passes using study hours and attendance.

from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

folder = Path(__file__).parent
df = pd.read_csv(folder / "students.csv")

print("First five rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())

# Features and target
X = df[["Hours_Studied", "Attendance"]]
y = df["Passed"]

# Keep the test data separate from the training data.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("tree", DecisionTreeClassifier(max_depth=3, random_state=42))
])
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("\nActual:", y_test.to_list())
print("Predicted:", predictions.tolist())
print("Accuracy:", round(accuracy_score(y_test, predictions), 2))
print("\nConfusion matrix:")
print(confusion_matrix(y_test, predictions))
print("\nClassification report:")
print(classification_report(y_test, predictions, zero_division=0))

# Predict for one new student using the same feature names.
new_student = pd.DataFrame({"Hours_Studied": [6], "Attendance": [85]})
result = model.predict(new_student)[0]
print("\nNew student prediction:", "Pass" if result == 1 else "Fail")
