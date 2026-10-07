# Week 5 - Day 3 - Accuracy Comparison
# Compare Decision Tree and Random Forest using the same cross-validation folds.

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier

X, y = load_iris(return_X_y=True)
folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
forest = RandomForestClassifier(n_estimators=50, random_state=42)

tree_scores = cross_val_score(tree, X, y, cv=folds)
forest_scores = cross_val_score(forest, X, y, cv=folds)

print("Decision Tree fold accuracies:", tree_scores.round(2))
print("Random Forest fold accuracies:", forest_scores.round(2))
print("Decision Tree average:", round(tree_scores.mean(), 2))
print("Random Forest average:", round(forest_scores.mean(), 2))
