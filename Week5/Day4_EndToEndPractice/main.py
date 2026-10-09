# Week 5 - Day 4 - End-to-End Practice
# Prepare data, train a model, predict, and evaluate.

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 6, 4, 7],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95, None, 88, 72, 92],
    "Department": ["HR", "IT", "HR", "IT", "HR", "IT", "HR", "IT", "HR", "IT", "HR", "IT"],
    "Passed": [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
})

X = df[["Hours", "Attendance", "Department"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

numbers = Pipeline([
    ("fill", SimpleImputer(strategy="mean")),
    ("scale", StandardScaler())
])

categories = OneHotEncoder(handle_unknown="ignore")

preprocessing = ColumnTransformer([
    ("numbers", numbers, ["Hours", "Attendance"]),
    ("categories", categories, ["Department"])
])

model = Pipeline([
    ("preprocessing", preprocessing),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Actual results:", y_test.to_list())
print("Predicted results:", predictions.tolist())
print("Accuracy:", round(accuracy_score(y_test, predictions), 2))
