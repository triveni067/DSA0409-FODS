import pandas as pd

data = pd.DataFrame({
    "customer_id": [1,2,3,4,5,6],
    "age": [25, 30, 25, 40, 30, 30]
})

age_freq = data["age"].value_counts()

print("Age Frequency Distribution:")
print(age_freq)
