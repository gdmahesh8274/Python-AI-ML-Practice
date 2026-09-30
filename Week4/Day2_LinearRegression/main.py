# Week 4 - Day 2 - Linear Regression Basics
# Train a simple linear regression model and generate predictions.

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [50, 55, 62, 68, 75, 82, 88, 95]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("Actual Marks:")
print(y.to_list())

print("\nPredicted Marks:")
print(predictions.round(2))

new_data = pd.DataFrame({"Hours_Studied": [9]})
print("\nPrediction for 9 study hours:", round(model.predict(new_data)[0], 2))
