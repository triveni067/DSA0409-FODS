# house_price_bivar_fixed.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv("houses.csv")

# Bivariate: size_sqft vs price
X = df[['size_sqft']].values   # numpy array -> avoids sklearn feature-name warnings
y = df['price'].values

model = LinearRegression()
model.fit(X, y)

print(f"Coefficient (slope): {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# Evaluate using train data
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))   # <- compatible replacement

print(f"R2 score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

# Save line plot
plt.scatter(X.flatten(), y)
plt.plot(X.flatten(), y_pred)
plt.xlabel("Size (sqft)")
plt.ylabel("Price")
plt.title("Size vs Price")
plt.savefig("size_price_plot.png")
print("\nSaved plot: size_price_plot.png")
