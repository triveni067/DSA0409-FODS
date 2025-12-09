import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv("student_scores.csv")
x = df['study_hours'].values
y = df['score'].values

corr, p = pearsonr(x,y)
print(f"Pearson correlation: {corr:.3f} (p-value: {p:.3f})")

plt.scatter(x,y)
m, b = np.polyfit(x,y,1)
plt.plot(x, m*x + b)
plt.xlabel("Study hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")
plt.savefig("study_vs_score.png")
print("Saved plot: study_vs_score.png")
