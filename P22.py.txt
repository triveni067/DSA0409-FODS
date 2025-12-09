import pandas as pd
from scipy import stats

data = pd.read_csv("customer_review.csv")["rating"]

mean = data.mean()
std = data.std()
n = len(data)
confidence = 0.95

t = stats.t.ppf((1 + confidence) / 2, n - 1)
margin = t * (std / (n ** 0.5))

print("Mean Rating:", mean)
print("95% Confidence Interval:", (mean - margin, mean + margin))
