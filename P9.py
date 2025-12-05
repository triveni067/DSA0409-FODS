import pandas as pd

property_data = pd.DataFrame({
    "property_id": [1,2,3,4],
    "location": ["A","B","A","C"],
    "bedrooms": [3,5,6,4],
    "area": [1200,2500,3000,1800],
    "price": [300000,550000,600000,400000]
})

avg_price_location = property_data.groupby("location")["price"].mean()
count_bedrooms = len(property_data[property_data["bedrooms"] > 4])
largest_area_property = property_data.loc[property_data["area"].idxmax()]

print(avg_price_location)
print(count_bedrooms)
print(largest_area_property)
