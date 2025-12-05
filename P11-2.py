import matplotlib.pyplot as plt

months = ["Week1","Week2","Week3","Week4"]
sales = [120, 150, 170, 200]

plt.scatter(months, sales)
plt.title("Monthly Sales - Scatter Plot")
plt.xlabel("Weeks")
plt.ylabel("Sales")
plt.show()
