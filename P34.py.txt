import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("treatment.csv")
X = df[['age','gender','bp','cholesterol']].values
y = (df['outcome'] == 'Good').astype(int).values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=1)

k = int(input("Enter k for KNN (e.g., 3): "))
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1:", f1_score(y_test, y_pred, zero_division=0))

# Show predictions on test set
res = pd.DataFrame(X_test, columns=['age','gender','bp','cholesterol'])
res['pred'] = y_pred
res['true'] = y_test
print("\nPredictions on test set:\n", res.to_string(index=False))
