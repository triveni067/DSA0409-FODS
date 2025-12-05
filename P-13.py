from collections import Counter
import string

file = open("sample_text.txt", "r")
text = file.read().lower()
file.close()

# Remove punctuation
for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()
frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)
