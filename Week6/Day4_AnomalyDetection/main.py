# Week 6 - Day 4 - Anomaly Detection
# Use Isolation Forest to find unusual data points.

import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.DataFrame({
    "Study_Hours": [2, 3, 4, 3, 5, 4, 2, 20],
    "Practice_Problems": [10, 12, 14, 11, 15, 13, 9, 100]
})

model = IsolationForest(contamination=0.125, random_state=42)
df["Anomaly"] = model.fit_predict(df)

print("Results (-1 means possible anomaly):")
print(df)
print("\nPossible anomalies:")
print(df[df["Anomaly"] == -1])
