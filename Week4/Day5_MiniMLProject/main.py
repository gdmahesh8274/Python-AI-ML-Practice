# Week 4 - Day 5 - Mini ML Project
# Build and evaluate two classification models using the Iris dataset.

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

logistic_model = LogisticRegression(max_iter=1000)
logistic_model.fit(X_train_scaled, y_train)
logistic_predictions = logistic_model.predict(X_test_scaled)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train_scaled, y_train)
knn_predictions = knn_model.predict(X_test_scaled)

logistic_accuracy = accuracy_score(y_test, logistic_predictions)
knn_accuracy = accuracy_score(y_test, knn_predictions)

print("Logistic Regression Accuracy:", round(logistic_accuracy, 2))
print("KNN Accuracy:", round(knn_accuracy, 2))

print("\nKNN Confusion Matrix:")
print(confusion_matrix(y_test, knn_predictions))

print("\nKNN Classification Report:")
print(classification_report(y_test, knn_predictions, target_names=data.target_names))

if knn_accuracy > logistic_accuracy:
    print("Best Model: KNN")
elif logistic_accuracy > knn_accuracy:
    print("Best Model: Logistic Regression")
else:
    print("Both models have the same accuracy.")
