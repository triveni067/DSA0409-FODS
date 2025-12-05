import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun"]
rainfall = [80, 60, 100, 120, 140, 160]

plt.scatter(months, rainfall)
plt.title("Monthly Rainfall - Scatter Plot")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.show()
