# Week 6 - Day 1 - Unsupervised Learning Introduction
# Unlike classification, clustering finds groups without target labels.

import pandas as pd
from sklearn.cluster import KMeans

customers = pd.DataFrame({
    "Annual_Spending": [10, 12, 15, 55, 58, 62],
    "Visits": [1, 2, 2, 8, 9, 10]
})

model = KMeans(n_clusters=2, random_state=42, n_init=10)
customers["Cluster"] = model.fit_predict(customers)

print("Customers grouped without a target column:")
print(customers)
print("\nCluster numbers are group IDs, not pass/fail labels.")
