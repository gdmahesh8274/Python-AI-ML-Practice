# Week 6 - Day 3 - Explained Variance
# Find how much information each principal component keeps.

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
scaled_data = StandardScaler().fit_transform(iris.data)

pca = PCA(n_components=4)
pca.fit(scaled_data)

print("Explained variance ratio by component:")
for number, ratio in enumerate(pca.explained_variance_ratio_, start=1):
    print("PC", number, ":", round(ratio, 3))

print("\nVariance kept by first two components:",
      round(sum(pca.explained_variance_ratio_[:2]) * 100, 2), "%")
