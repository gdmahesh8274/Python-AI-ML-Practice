# Week 3 - Day 3 - Distribution Analysis
# Analyze a numerical column and compare mean and median.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

marks = [55, 60, 65, 70, 72, 75, 78, 80, 82, 85, 88, 90, 95, 98, 100]
df = pd.DataFrame({"Marks": marks})

mean_value = df["Marks"].mean()
median_value = df["Marks"].median()

print("Mean:", round(mean_value, 2))
print("Median:", median_value)

sns.histplot(data=df, x="Marks", bins=6, kde=True)
plt.axvline(mean_value, label="Mean")
plt.axvline(median_value, linestyle="--", label="Median")
plt.title("Marks Distribution")
plt.legend()
plt.show()

print("\nObservation:")
print("The mean and median are close, so the distribution is fairly balanced.")
