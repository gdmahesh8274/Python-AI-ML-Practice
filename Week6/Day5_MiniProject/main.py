# Week 6 - Day 5: Customer Segmentation Mini Project
# Group customers by income and spending score using K-Means.

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

folder = Path(__file__).parent
df = pd.read_csv(folder / "customers.csv")
features = ["Annual_Income", "Spending_Score"]

print("First five customers:")
print(df.head())
print("\nMissing values:")
print(df.isna().sum())

# Scale the features so both columns contribute fairly to distance.
scaler = StandardScaler()
scaled = scaler.fit_transform(df[features])

# Elbow method: compare how inertia changes with k.
inertias = []
cluster_counts = range(1, 7)
for k in cluster_counts:
    model = KMeans(n_clusters=k, n_init=10, random_state=42)
    model.fit(scaled)
    inertias.append(model.inertia_)
    print("k =", k, "inertia =", round(model.inertia_, 2))

plt.figure()
plt.plot(list(cluster_counts), inertias, marker="o")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Customer Segmentation")
plt.grid(True)
plt.tight_layout()
plt.savefig(folder / "elbow_plot.png")
plt.close()

# This sample dataset was designed with three visible customer groups.
model = KMeans(n_clusters=3, n_init=10, random_state=42)
df["Cluster"] = model.fit_predict(scaled)

print("\nCustomers with cluster labels:")
print(df.to_string(index=False))
print("\nNumber of customers per cluster:")
print(df["Cluster"].value_counts().sort_index())
print("\nAverage values per cluster:")
print(df.groupby("Cluster")[features].mean().round(2))

# Plot in the original units, with centers converted back to original units.
centers = scaler.inverse_transform(model.cluster_centers_)
plt.figure()
plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"], cmap="viridis")
plt.scatter(centers[:, 0], centers[:, 1], marker="X", s=180, c="red", label="Centers")
plt.xlabel("Annual Income (sample units)")
plt.ylabel("Spending Score")
plt.title("Customer Segments")
plt.legend()
plt.tight_layout()
plt.savefig(folder / "customer_clusters.png")
plt.close()

df.to_csv(folder / "customer_segments.csv", index=False)
print("\nSaved elbow_plot.png, customer_clusters.png, and customer_segments.csv")
