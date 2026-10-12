# Week 6 - Day 1 - K-Means Basics
# Group sample data into two clusters.

import pandas as pd
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Hours_Studied": [1, 2, 2, 7, 8, 9],
    "Practice_Problems": [2, 3, 2, 8, 9, 9]
})

model = KMeans(n_clusters=2, random_state=42, n_init=10)
data["Cluster"] = model.fit_predict(data)

print("Cluster assignments:")
print(data)
print("\nCluster centers:")
print(model.cluster_centers_.round(2))
