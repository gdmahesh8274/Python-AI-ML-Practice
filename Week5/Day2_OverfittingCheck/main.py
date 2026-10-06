# Week 5 - Day 2 - Overfitting Check
# Compare training and testing accuracy.

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

train_accuracy = accuracy_score(y_train, train_predictions)
test_accuracy = accuracy_score(y_test, test_predictions)

print("Training Accuracy:", round(train_accuracy, 2))
print("Testing Accuracy:", round(test_accuracy, 2))
print("Accuracy Difference:", round(train_accuracy - test_accuracy, 2))

if train_accuracy > test_accuracy:
    print("Higher training accuracy can be a sign of overfitting.")
else:
    print("Training and testing performance are similar.")
