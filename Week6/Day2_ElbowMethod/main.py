# Week 6 - Day 2 - Elbow Method
# Plot inertia for different numbers of K-Means clusters.

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.7, random_state=42)

cluster_counts = range(1, 9)
inertias = []

for k in cluster_counts:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X)
    inertias.append(model.inertia_)
    print("Clusters:", k, "Inertia:", round(model.inertia_, 2))

plt.plot(list(cluster_counts), inertias, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.show()

print("Look for the bend in the curve to choose a useful k.")
