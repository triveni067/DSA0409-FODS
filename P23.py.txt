import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

df = pd.read_csv("treatment_data.csv")

control = df[df["group"]=="control"]["value"]
treat = df[df["group"]=="treatment"]["value"]

t, p = ttest_ind(control, treat)

plt.boxplot([control, treat], tick_labels=["Control", "Treatment"])
plt.title("Clinical Trial Results")
plt.ylabel("Values")
plt.show()

print("p-value:", p)
