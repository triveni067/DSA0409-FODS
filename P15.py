import pandas as pd

posts = pd.DataFrame({
    "post_id": [1,2,3,4,5,6],
    "likes": [10, 20, 10, 15, 20, 10]
})

like_freq = posts["likes"].value_counts()

print("Likes Frequency Distribution:")
print(like_freq)
