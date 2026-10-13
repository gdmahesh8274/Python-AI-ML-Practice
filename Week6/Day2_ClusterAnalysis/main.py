# Week 6 - Day 2 - Cluster Analysis
# Compare the size and average values of each cluster.

import pandas as pd
from sklearn.cluster import KMeans

df = pd.DataFrame({
    "Annual_Spending": [10, 12, 15, 20, 55, 60, 65, 70],
    "Store_Visits": [1, 2, 2, 3, 8, 9, 9, 10]
})

model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(df[["Annual_Spending", "Store_Visits"]])

print("Customer clusters:")
print(df)

print("\nNumber of customers in each cluster:")
print(df["Cluster"].value_counts().sort_index())

print("\nAverage values for each cluster:")
print(df.groupby("Cluster")[["Annual_Spending", "Store_Visits"]].mean().round(2))
print("\nCluster IDs are arbitrary group labels.")
