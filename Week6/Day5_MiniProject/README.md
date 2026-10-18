# Customer Segmentation - Week 6 Day 5

This mini project uses **K-Means clustering** to group customers based on annual income and spending score. The dataset is synthetic and for learning only.

## Run

Install dependencies:

```bash
pip install pandas scikit-learn matplotlib
```

Then run:

```bash
python main.py
```

## Workflow

1. Read `customers.csv` and check for missing values.
2. Standardize income and spending score using `StandardScaler`.
3. Plot K-Means inertia for k = 1 to 6 (elbow method).
4. Fit K-Means with three clusters for this teaching dataset.
5. Print cluster sizes and average customer characteristics.
6. Save a cluster plot and a CSV with the cluster labels.

## Generated files

Running the script creates `elbow_plot.png`, `customer_clusters.png`, and `customer_segments.csv` in this folder.

Cluster numbers are arbitrary labels. They do not indicate customer quality or a ranking.
