# Week 4 - Day 1 - Scikit-learn Basics Setup
# Basic machine learning workflow: fit, predict, and evaluate.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [50, 55, 62, 68, 75, 82, 88, 95]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Predict values
predictions = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)

print("Actual Values:")
print(y_test.to_list())

print("\nPredicted Values:")
print(predictions)

print("\nMean Absolute Error:", round(mae, 2))
