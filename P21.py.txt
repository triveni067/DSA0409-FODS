import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv("rare_elements.csv")["concentration"]

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (0.90, 0.95, 0.99): "))
precision = float(input("Enter desired precision: "))

sample = data.sample(n, replace=True)   # FIXED
mean = np.mean(sample)
std = np.std(sample, ddof=1)

t = stats.t.ppf((1 + confidence) / 2, n - 1)
margin = t * (std / np.sqrt(n))

print("Sample Mean:", mean)
print("Confidence Interval:", (mean - margin, mean + margin))
print("Precision Achieved:", margin)

