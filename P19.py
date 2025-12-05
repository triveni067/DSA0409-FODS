import pandas as pd

df = pd.read_csv("sales_data.csv")

df["Total Sales"] = df["Quantity Sold"] * df["Unit Price"]

product_sales = df.groupby("Product")["Total Sales"].sum()
profit = product_sales * 0.20

print(profit.sort_values(ascending=False).head(5))
