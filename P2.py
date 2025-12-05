import numpy as np

sales_data = np.array([
    [1200, 1350, 1400],
    [900, 1100, 1500],
    [1000, 1150, 1300]
])

avg_price = np.mean(sales_data)
print("Average product price:", avg_price)
