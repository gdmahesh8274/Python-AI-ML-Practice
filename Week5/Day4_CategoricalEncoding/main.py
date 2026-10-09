# Week 5 - Day 4 - Categorical Encoding
# Convert categories into numerical columns with one-hot encoding.

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame({
    "Department": ["IT", "HR", "Sales", "IT", "HR"]
})

print("Original categories:")
print(df)

encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
encoded = encoder.fit_transform(df[["Department"]])

encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(["Department"])
)

print("\nEncoded data:")
print(encoded_df)
