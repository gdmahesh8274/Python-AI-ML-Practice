# Week 3 - Day 3 - Categorical Analysis
# Analyze categories using counts and average values.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales"],
    "Marks": [85, 78, 92, 80, 82, 88, 76]
}

df = pd.DataFrame(data)

print("Category Counts:")
print(df["Department"].value_counts())

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

sns.countplot(data=df, x="Department")
plt.title("Student Count by Department")
plt.show()

sns.barplot(data=df, x="Department", y="Marks")
plt.title("Average Marks by Department")
plt.show()
