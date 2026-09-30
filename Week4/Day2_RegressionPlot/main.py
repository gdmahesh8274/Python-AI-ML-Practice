# Week 4 - Day 2 - Regression Visualization
# Plot actual and predicted values.

import pandas as pd
import matplotlib.pyplot as plt
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

plt.scatter(df["Hours_Studied"], y, label="Actual")
plt.plot(df["Hours_Studied"], predictions, label="Predicted")

plt.title("Actual vs Predicted Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
