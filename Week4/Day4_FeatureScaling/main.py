# Week 4 - Day 4 - Feature Scaling Basics
# Scale features using StandardScaler before training KNN.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

data = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

accuracy = model.score(X_test_scaled, y_test)

print("First scaled training row:")
print(X_train_scaled[0])

print("\nKNN Accuracy after scaling:", round(accuracy, 2))
