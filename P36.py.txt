import pandas as pd
import numpy as np

df = pd.read_csv("stock_prices.csv", parse_dates=['date'])
df = df.sort_values('date')

df['daily_return'] = df['close'].pct_change()
volatility = df['daily_return'].std()  # sample std of returns
price_range = df['close'].max() - df['close'].min()

print(f"Number of days: {len(df)}")
print(f"Mean closing price: {df['close'].mean():.2f}")
print(f"Standard deviation of daily returns (volatility): {volatility:.4f}")
print(f"Price range (max - min): {price_range:.2f}")

# Save summary
summary = {
    'mean_close': df['close'].mean(),
    'volatility': volatility,
    'price_range': price_range
}
pd.Series(summary).to_csv("stock_summary.csv")
print("\nSaved summary to stock_summary.csv")
