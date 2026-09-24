# Week 3 - Day 3 - Correlation Heatmap
# Create a correlation matrix and visualize it with a heatmap.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6],
    "Attendance": [60, 65, 70, 78, 85, 92],
    "Marks": [50, 58, 65, 72, 82, 90]
}

df = pd.DataFrame(data)

correlation = df.corr()

print("Correlation Matrix:")
print(correlation)

sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()
