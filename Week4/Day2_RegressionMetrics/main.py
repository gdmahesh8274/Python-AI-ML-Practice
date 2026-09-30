# Week 4 - Day 2 - MAE and MSE
# Evaluate regression predictions using MAE and MSE.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [48, 55, 60, 66, 73, 79, 85, 90, 94, 98]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)

print("Actual Values:", y_test.to_list())
print("Predicted Values:", predictions.round(2))
print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
