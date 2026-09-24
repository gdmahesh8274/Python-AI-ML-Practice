# Week 3 - Day 3 - Seaborn Basics
# Practice count plots, box plots, and pair plots.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR"],
    "Age": [22, 25, 24, 28, 23, 27],
    "Marks": [85, 78, 92, 80, 88, 75]
}

df = pd.DataFrame(data)

sns.countplot(data=df, x="Department")
plt.title("Students by Department")
plt.show()

sns.boxplot(data=df, x="Department", y="Marks")
plt.title("Marks by Department")
plt.show()

sns.pairplot(df, hue="Department")
plt.show()
