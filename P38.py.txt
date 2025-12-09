import pandas as pd
import numpy as np

df = pd.read_csv("city_temps.csv")
group = df.groupby('city')['temp']

mean_temp = group.mean()
std_temp = group.std()
temp_range = group.max() - group.min()

print("Mean temperature per city:\n", mean_temp)
print("\nStandard deviation per city:\n", std_temp)
print("\nTemperature range per city:\n", temp_range)

most_range_city = temp_range.idxmax()
most_consistent_city = std_temp.idxmin()
print(f"\nCity with highest range: {most_range_city}")
print(f"Most consistent city (lowest std): {most_consistent_city}")
