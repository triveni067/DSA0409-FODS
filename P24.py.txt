import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
df = pd.read_csv("patient_data.csv")

# Convert to numpy arrays to avoid feature name warnings
X = df[['symptom1', 'symptom2', 'symptom3']].values
y = df['label'].values

# Train model
k = int(input("Enter value of k: "))
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

# User input
s1 = float(input("Enter symptom 1: "))
s2 = float(input("Enter symptom 2: "))
s3 = float(input("Enter symptom 3: "))

# Prediction using numpy array
prediction = model.predict([[s1, s2, s3]])

print("Prediction (0 = No condition, 1 = Condition):", prediction[0])
