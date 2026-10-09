# Week 5 - Day 4 - Preprocessing Revision
# Fill missing values and scale numerical features.

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "Age": [20, 22, None, 25, 24],
    "Study_Hours": [2, 4, 3, None, 5]
})

print("Original data:")
print(df)

imputer = SimpleImputer(strategy="mean")
filled_data = imputer.fit_transform(df)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(filled_data)

print("\nAfter filling missing values:")
print(pd.DataFrame(filled_data, columns=df.columns))

print("\nAfter scaling:")
print(pd.DataFrame(scaled_data, columns=df.columns).round(2))
