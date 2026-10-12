# Week 6 - Day 1 - Cluster Visualization
# Plot K-Means groups using different colors.

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

data = pd.DataFrame({
    "Hours_Studied": [1, 2, 2, 3, 7, 8, 8, 9],
    "Practice_Problems": [2, 3, 2, 4, 7, 8, 9, 9]
})

model = KMeans(n_clusters=2, random_state=42, n_init=10)
labels = model.fit_predict(data)

plt.scatter(data["Hours_Studied"], data["Practice_Problems"], c=labels, cmap="viridis")
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
            marker="X", s=180, c="red", label="Centers")
plt.title("K-Means Clusters")
plt.xlabel("Hours Studied")
plt.ylabel("Practice Problems")
plt.legend()
plt.show()
