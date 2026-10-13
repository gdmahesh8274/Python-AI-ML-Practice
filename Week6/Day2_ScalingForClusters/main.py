# Week 6 - Day 2 - Scaling for Clusters
# Standardize features before K-Means so units are comparable.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "Annual_Income": [20000, 25000, 30000, 80000, 90000, 100000],
    "Store_Visits": [2, 3, 4, 8, 9, 10]
})

features = df[["Annual_Income", "Store_Visits"]]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

model = KMeans(n_clusters=2, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(scaled_features)

print("Scaled feature values:")
print(pd.DataFrame(scaled_features, columns=features.columns).round(2))

print("\nCluster assignments:")
print(df)
