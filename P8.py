import pandas as pd

sales = pd.DataFrame({
    "product": ["A","B","A","C","B","D","A"],
    "quantity": [5,3,2,7,1,4,6]
})

top5 = sales.groupby("product")["quantity"].sum().sort_values(ascending=False).head(5)
print(top5)
