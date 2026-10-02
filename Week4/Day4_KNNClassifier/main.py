# Week 4 - Day 4 - KNN Classifier
# Train a K-Nearest Neighbors classifier and make predictions.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Values:")
print(y_test[:10])

print("\nPredicted Values:")
print(predictions[:10])
