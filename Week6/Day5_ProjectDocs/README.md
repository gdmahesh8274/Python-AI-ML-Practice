# Week 6 Day 5 - Cluster Analysis Report

## Objective

Segment customers into groups with similar income and spending behavior using unsupervised machine learning.

## Dataset

`Week6/Day5_MiniProject/customers.csv` contains 18 synthetic customers with `Customer_ID`, `Annual_Income`, and `Spending_Score`. The ID is not used for clustering.

## Preprocessing

Check missing values and scale the two numeric features with `StandardScaler`. Scaling prevents differences in measurement ranges from dominating K-Means distances.

## Method

Calculate inertia for k = 1 through 6 and save an elbow plot. For this intentionally simple teaching dataset, fit K-Means with k = 3, `n_init=10`, and `random_state=42`.

## Analysis

The dataset was constructed with three broad patterns: lower income/lower spending, medium income/medium spending, and higher income/higher spending. Run `main.py` to see the computed group sizes and averages. Cluster IDs can be assigned in any order, so interpret each cluster using its mean feature values rather than its number.

## Outputs

- `elbow_plot.png`: inertia by number of clusters
- `customer_clusters.png`: scatter plot of customer groups and cluster centers
- `customer_segments.csv`: customer data with assigned cluster labels

These outputs are generated when the script is run; they are not precomputed in the repository.

## Limitations

This small synthetic dataset has clear patterns by design. Real customer segmentation requires larger, representative data and careful checks of cluster stability and business relevance.
