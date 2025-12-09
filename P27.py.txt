import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("customer_churn.csv")

# Convert to numpy arrays to avoid warning
X = df[['usage', 'contract', 'age']].values
y = df['churn'].values

model = LogisticRegression()
model.fit(X, y)

usage = float(input("Enter usage minutes: "))
contract = int(input("Enter contract duration: "))
age = int(input("Enter age: "))

# Prediction (safe, no warning)
prediction = model.predict([[usage, contract, age]])

print("Churn Prediction (0 = No, 1 = Yes):", prediction[0])
