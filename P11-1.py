import matplotlib.pyplot as plt

months = ["Week1","Week2","Week3","Week4"]
sales = [120, 150, 170, 200]

plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Weeks")
plt.ylabel("Sales")
plt.show()
