# Week 3 - Day 4 - EDA Summary
# Create charts and write five key observations about a small dataset.

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Mahesh", "John", "Sara", "David", "Emma"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Hours_Studied": [5, 3, 7, 4, 6],
    "Marks": [85, 70, 95, 78, 90]
}

df = pd.DataFrame(data)

# Chart 1: Marks by student
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

# Chart 2: Study hours vs marks
plt.scatter(df["Hours_Studied"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()

print("Five EDA Observations:")
print("1. Sara has the highest marks.")
print("2. John has the lowest marks.")
print("3. Students who studied more hours generally scored higher.")
print("4. IT students have higher marks in this sample.")
print("5. Marks range from 70 to 95.")
