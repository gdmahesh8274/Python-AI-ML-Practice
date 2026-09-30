# Week 4 - Day 3 - Logistic Regression Basics
# Build a logistic regression model using a binary classification dataset.

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Values:")
print(y_test[:10])

print("\nPredicted Values:")
print(predictions[:10])
