import numpy as np

sales_data = np.array([25000, 30000, 35000, 45000])

total_sales = np.sum(sales_data)
percent_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print("Total yearly sales:", total_sales)
print("Percentage increase Q1 to Q4:", percent_increase, "%")
