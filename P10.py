import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales = [200, 300, 250, 400, 450]

plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
