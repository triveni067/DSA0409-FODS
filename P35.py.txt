import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("transactions.csv")
# Aggregate per customer
agg = df.groupby('customer_id').agg({
    'amount':'sum','items':'sum','visits':'sum'
}).reset_index()

X = agg[['amount','items','visits']].values
X = StandardScaler().fit_transform(X)

k = int(input("Enter k for segmentation (e.g., 3): "))
model = KMeans(n_clusters=k, random_state=0, n_init=10)
agg['cluster'] = model.fit_predict(X)

print(agg.to_string(index=False))
agg.to_csv("customer_segments_store.csv", index=False)
print("\nSaved: customer_segments_store.csv")
