# Week 6 - Day 3 - PCA Projection
# Visualize the Iris dataset on two principal components.

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
scaled_data = StandardScaler().fit_transform(iris.data)
points = PCA(n_components=2).fit_transform(scaled_data)

plt.scatter(points[:, 0], points[:, 1], c=iris.target, cmap="viridis")
plt.title("Iris PCA Projection")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label="Iris species")
plt.grid(True)
plt.show()
