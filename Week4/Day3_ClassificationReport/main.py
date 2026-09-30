# Week 4 - Day 3 - Classification Report
# Evaluate classification using precision, recall, and F1-score.

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, predictions, target_names=data.target_names))
