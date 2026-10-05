# Week 5 - Day 1 - Decision Tree
# Build and evaluate a basic Decision Tree classifier.

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Actual Values:")
print(y_test[:10])

print("\nPredicted Values:")
print(predictions[:10])

print("\nDecision Tree Accuracy:", round(accuracy, 2))
