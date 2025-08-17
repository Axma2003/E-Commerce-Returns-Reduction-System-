import pandas as pd

# Load data
reviews = pd.read_csv('../data/product_reviews.csv')
returns = pd.read_csv('../data/customer_returns.csv')

# Merge datasets
df = pd.merge(reviews, returns, on='product_id', how='left')

# Basic preprocessing
df['review_text'] = df['review_text'].str.lower()
df['return_flag'] = df['return_reason'].notnull().astype(int)

df.to_csv('../data/processed_data.csv', index=False)
print("Data preprocessed and saved.")
