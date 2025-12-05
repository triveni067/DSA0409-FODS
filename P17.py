import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

stop_words = ["the","and","is","a","to","of","in"]
text = " ".join(df["feedback"]).lower()
text = text.translate(str.maketrans("", "", string.punctuation))
words = [w for w in text.split() if w not in stop_words]

freq = Counter(words)
N = int(input("Enter N: "))
topN = freq.most_common(N)

print(topN)

labels, values = zip(*topN)
colors = ["red", "blue", "green", "orange", "purple"]
plt.bar(labels, values, color=colors)
plt.show()
