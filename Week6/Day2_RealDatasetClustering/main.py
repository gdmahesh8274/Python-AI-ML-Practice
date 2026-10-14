# Week 6 - Day 2 - Real Dataset Clustering
# Group Iris flower measurements without using the species labels to train.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris(as_frame=True)
features = iris.data

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = model.fit_predict(scaled_features)

result = features.copy()
result["Cluster"] = clusters

print("First 10 rows with cluster labels:")
print(result.head(10))

print("\nNumber of flowers in each cluster:")
print(result["Cluster"].value_counts().sort_index())

print("\nAverage flower measurements by cluster:")
print(result.groupby("Cluster").mean().round(2))

print("\nThe Iris species labels were not used for clustering.")
