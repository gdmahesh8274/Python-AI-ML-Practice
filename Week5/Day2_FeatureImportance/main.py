# Week 5 - Day 2 - Feature Importance
# Display feature importance from a Random Forest model.

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Feature Importance:")
for name, importance in zip(data.feature_names, model.feature_importances_):
    print(name, ":", round(importance, 3))

most_important = data.feature_names[model.feature_importances_.argmax()]
print("\nMost Important Feature:", most_important)
