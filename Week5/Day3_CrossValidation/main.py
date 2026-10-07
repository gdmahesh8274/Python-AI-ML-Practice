# Week 5 - Day 3 - Cross Validation
# Evaluate a Decision Tree using five folds.

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
model = DecisionTreeClassifier(random_state=42)
scores = cross_val_score(model, X, y, cv=5)

print("Fold accuracies:", scores.round(2))
print("Average accuracy:", round(scores.mean(), 2))
