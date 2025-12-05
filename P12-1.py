import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
temperature = [22, 24, 28, 30, 32, 35]

plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature - Line Plot")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.show()
