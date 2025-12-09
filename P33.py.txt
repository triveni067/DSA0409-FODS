import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("cars.csv")
features = ['engine_cc','horsepower','fuel_efficiency','age']
X = df[features].values
y = df['price'].values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("R2:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# Feature importance via coefficients
for feat, coef in zip(features, model.coef_):
    print(f"{feat}: {coef:.2f}")
