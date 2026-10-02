# Week 4 - Day 4 - Practice Dataset
# Apply a complete classification workflow to the Wine dataset.

from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

data = load_wine()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, predictions)

print("Dataset:", data.DESCR.splitlines()[0])
print("Number of features:", X.shape[1])
print("Number of classes:", len(data.target_names))
print("Accuracy:", round(accuracy, 2))

print("\nFirst 10 Predictions:")
print(predictions[:10])
