from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# User inputs
sl = float(input("Enter sepal length: "))
sw = float(input("Enter sepal width: "))
pl = float(input("Enter petal length: "))
pw = float(input("Enter petal width: "))

prediction = model.predict([[sl, sw, pl, pw]])
print("Predicted species:", iris.target_names[prediction][0])
