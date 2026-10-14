# Week 6 - Day 3 - PCA Basics
# Reduce the Iris dataset from four features to two components.

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
scaled_data = StandardScaler().fit_transform(iris.data)

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

print("Original shape:", iris.data.shape)
print("Reduced shape:", reduced_data.shape)
print("\nFirst five rows after PCA:")
print(reduced_data[:5].round(2))
