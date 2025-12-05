import numpy as np

fuel_efficiency = np.array([18, 20, 22, 25, 30])

avg_eff = np.mean(fuel_efficiency)

model1 = fuel_efficiency[1]   # Example model A
model2 = fuel_efficiency[4]   # Example model B

improvement = ((model2 - model1) / model1) * 100

print("Average Fuel Efficiency:", avg_eff)
print("Percentage Improvement:", improvement, "%")
