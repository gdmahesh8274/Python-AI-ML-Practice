###Array
ages = [20, 25, 30]

print(ages)

####Dataframe
import pandas as pd

df = pd.DataFrame({
    "name": ["John", "Sam"],
    "age": [25, 30]
})

print(df)

###Filtering
print(df[df["age"] > 25])

###Statistics
print(df["age"].mean())