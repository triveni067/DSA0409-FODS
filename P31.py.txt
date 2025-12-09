import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("ecom_customers.csv")
X = df[['recency','frequency','monetary','age']].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = int(input("Enter number of clusters (e.g., 3): "))
model = KMeans(n_clusters=k, random_state=42, n_init=10)
model.fit(X_scaled)

df['cluster'] = model.predict(X_scaled)
print("\nCustomerID -> Cluster")
print(df[['customer_id','cluster']].to_string(index=False))

# Save cluster assignment
df.to_csv("ecom_customers_segmented.csv", index=False)
print("\nSaved segmented file: ecom_customers_segmented.csv")
