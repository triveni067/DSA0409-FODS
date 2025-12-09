import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("transactions2.csv")
X = df[['total_spent','num_items']].values
X_scaled = StandardScaler().fit_transform(X)

k = int(input("Enter k (e.g., 3): "))
model = KMeans(n_clusters=k, random_state=42, n_init=10)
df['cluster'] = model.fit_predict(X_scaled)

print(df.to_string(index=False))
plt.scatter(df['total_spent'], df['num_items'], c=df['cluster'])
plt.xlabel("Total Spent")
plt.ylabel("Num Items")
plt.title("Customer Clusters")
plt.savefig("customer_clusters.png")
print("\nSaved cluster plot: customer_clusters.png")
