reviews = [
    "The product is good and the quality is good",
    "I like the product",
    "The product is not bad"
]

words = " ".join(reviews).lower().split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)
