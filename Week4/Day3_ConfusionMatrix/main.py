# Week 4 - Day 3 - Confusion Matrix
# Generate a confusion matrix and understand TN, FP, FN, and TP.

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

matrix = confusion_matrix(y_test, predictions)
tn, fp, fn, tp = matrix.ravel()

print("Confusion Matrix:")
print(matrix)

print("\nTrue Negative:", tn)
print("False Positive:", fp)
print("False Negative:", fn)
print("True Positive:", tp)
