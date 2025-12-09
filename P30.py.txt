import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text

df = pd.read_csv("car_data.csv")

# Convert to numpy to avoid feature name warnings
X = df[['mileage', 'age', 'brand', 'engine']].values
y = df['price'].values

model = DecisionTreeRegressor()
model.fit(X, y)

mileage = float(input("Enter mileage: "))
age = float(input("Enter age: "))
brand = int(input("Enter brand (1/2/3): "))
engine = int(input("Enter engine type (1/2): "))

# Prediction (no warning)
prediction = model.predict([[mileage, age, brand, engine]])
print("Predicted Car Price =", prediction[0])

# Display decision path
tree_rules = export_text(model, feature_names=None)
print("\nDecision Path:\n", tree_rules)
