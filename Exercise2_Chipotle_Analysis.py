import pandas as pd
import numpy as np

# Load dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
food = pd.read_csv(url, sep='\t')

# Data exploration
print(food.head())
print(food.tail())
print(food.columns)
print(food.isna().sum())
print(food.duplicated().sum())

# Fill NaN values
food.fillna('Not specified', inplace=True)

# Check column types
print(food.dtypes)

# Convert price column to float
food['item_price'] = food['item_price'].str.replace('$','').astype(float)

# Create new column: price per item
food['price_per_item'] = food['item_price'] / food['quantity']

# Display statistics
print(food.describe())

# Most ordered items
print(food.groupby('item_name')['quantity'].sum().sort_values(ascending=False).head(10))

# Total number of items ordered
print(food['quantity'].sum())

# Total revenue
print(food['item_price'].sum())

# Average revenue per order
print(food.groupby('order_id')['item_price'].sum().mean())

# Save cleaned dataset
food.to_csv('data/Exercise2_Cleaned.csv', index=False)
