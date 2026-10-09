# Week 5 - Day 4 - Pipeline Basics
# Combine scaling and classification in one pipeline.

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=3))
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

print("Pipeline accuracy:", round(accuracy_score(y_test, predictions), 2))
