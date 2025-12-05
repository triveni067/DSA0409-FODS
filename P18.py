import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    "age": [23,25,27,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59],
    "fat": [15,16,17,18,20,22,23,24,25,26,27,29,30,31,33,35,36,37]
}

df = pd.DataFrame(data)

# Mean, Median, Std
print("Mean:\n", df.mean())
print("\nMedian:\n", df.median())
print("\nStandard Deviation:\n", df.std())

# ------ Create One Page with 3 Plots ------
plt.figure(figsize=(12, 10))

# 1. Boxplot (updated line)
plt.subplot(2, 2, 1)
plt.boxplot([df["age"], df["fat"]], tick_labels=["Age", "%Fat"])
plt.title("Boxplot for Age and %Fat")

# 2. Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(df["age"], df["fat"])
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.title("Scatter Plot")

# 3. Q-Q Plot (Manual using NumPy)
plt.subplot(2, 1, 2)
ages = np.sort(df["age"])
n = len(ages)
prob = (np.arange(1, n+1) - 0.5) / n
theoretical_quantiles = np.quantile(np.random.normal(0, 1, 5000), prob)

plt.scatter(theoretical_quantiles, ages)
plt.plot(theoretical_quantiles, theoretical_quantiles, color="red")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Age")
plt.title("Q-Q Plot (Age)")

plt.tight_layout()
plt.show()
