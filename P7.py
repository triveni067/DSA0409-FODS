import pandas as pd

order_data = pd.DataFrame({
    "customer_id": [1,1,2,2,3],
    "order_date": pd.to_datetime(["2024-01-01","2024-01-15","2024-01-05","2024-01-20","2024-01-18"]),
    "product_name": ["Apple","Banana","Apple","Mango","Banana"],
    "order_quantity": [2,3,1,5,4]
})

orders_per_customer = order_data.groupby("customer_id")["order_date"].count()
avg_qty_per_product = order_data.groupby("product_name")["order_quantity"].mean()
earliest_date = order_data["order_date"].min()
latest_date = order_data["order_date"].max()

print(orders_per_customer)
print(avg_qty_per_product)
print(earliest_date, latest_date)
