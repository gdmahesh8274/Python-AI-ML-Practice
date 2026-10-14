# Week 6 - Day 3 - Clustering with PCA
# Scale the Iris data, apply PCA, then find clusters with K-Means.

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
scaled_data = StandardScaler().fit_transform(iris.data)

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

model = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = model.fit_predict(reduced_data)

print("Cluster labels for first 10 flowers:", clusters[:10])
print("Cluster counts:")
for label in range(3):
    print("Cluster", label, ":", (clusters == label).sum())

plt.scatter(reduced_data[:, 0], reduced_data[:, 1],
            c=clusters, cmap="viridis")
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
            c="red", marker="X", s=150, label="Centers")
plt.title("K-Means Clusters after PCA")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.show()
