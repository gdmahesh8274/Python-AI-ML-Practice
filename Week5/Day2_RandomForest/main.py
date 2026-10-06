# Week 5 - Day 2 - Random Forest
# Build and evaluate a Random Forest classifier.

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

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Actual Values:", y_test[:10])
print("Predicted Values:", predictions[:10])
print("Random Forest Accuracy:", round(accuracy, 2))
