# Week 5 - Day 3 - Best Parameters
# Find the best Random Forest settings with GridSearchCV.

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

X, y = load_iris(return_X_y=True)
model = RandomForestClassifier(random_state=42)
parameters = {"n_estimators": [20, 50], "max_depth": [2, 4, None]}

search = GridSearchCV(model, parameters, cv=5, scoring="accuracy")
search.fit(X, y)

print("Best parameters:", search.best_params_)
print("Best average validation accuracy:", round(search.best_score_, 2))
