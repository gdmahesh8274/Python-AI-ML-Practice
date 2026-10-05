import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the data
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")
df = pd.read_csv(csv_path)

# 2. Look at the data
print(df.head())

# Check basic information
print(df.info())

# Check missing values
print(df.isnull().sum())

# 3. Simple summary
print(df.describe())

# 4. Create a chart
df["Age"].hist()

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()

# 5. Simple finding
print("Average Age:", df["Age"].mean())
print("Highest Age:", df["Age"].max())
print("Lowest Age:", df["Age"].min())