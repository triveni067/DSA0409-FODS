import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("customer_segments.csv")

# Convert to numpy arrays to avoid warning
X = df[['feature1', 'feature2']].values

model = KMeans(n_clusters=2)
model.fit(X)

f1 = float(input("Enter feature 1: "))
f2 = float(input("Enter feature 2: "))

# Predict (no warning)
cluster = model.predict([[f1, f2]])

print("Assigned Cluster:", cluster[0])
