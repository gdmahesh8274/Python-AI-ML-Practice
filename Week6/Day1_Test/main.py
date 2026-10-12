# Week 6 - Day 1 - Test: Trees, Random Forest and Preprocessing
# Quick revision of classification and feature scaling.

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)

forest = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(n_estimators=50, random_state=42))
])
forest.fit(X_train, y_train)

print("Decision Tree accuracy:", round(accuracy_score(y_test, tree.predict(X_test)), 2))
print("Random Forest accuracy:", round(accuracy_score(y_test, forest.predict(X_test)), 2))
print("Revision: train/test split, scaling, decision trees and random forests.")
