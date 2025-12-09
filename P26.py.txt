import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_data.csv")

# Convert to numpy arrays (fix warning)
X = df[['area', 'bedrooms', 'location']].values
y = df['price'].values

model = LinearRegression()
model.fit(X, y)

# User input
area = float(input("Enter area: "))
bed = int(input("Enter bedrooms: "))
loc = int(input("Enter location (1/2/3): "))

# Prediction (list is fine because training had no feature names)
prediction = model.predict([[area, bed, loc]])

print("Predicted Price =", prediction[0])

