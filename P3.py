import numpy as np

# Example data: [bedrooms, sqft, price]
house_data = np.array([
    [3, 1800, 250000],
    [5, 2500, 480000],
    [6, 3000, 550000],
    [4, 2000, 300000]
])

filtered = house_data[house_data[:, 0] > 4]
avg_price = np.mean(filtered[:, 2])

print("Average price of houses with >4 bedrooms:", avg_price)
