import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Download gold futures data
gold = yf.download("GC=F", start="2018-01-01")

# Remove MultiIndex columns
if isinstance(gold.columns, pd.MultiIndex):
    gold.columns = gold.columns.get_level_values(0)

# Display first rows
print(gold.head())

# Basic statistics
average_price = gold["Close"].mean()
print(f"Average Gold Price: {average_price:.2f}")
max_price=gold["Close"].max()
print(f"Maximum Gold Price: {max_price:.2f}")
min_price=gold["Close"].min()
print(f"Minimum Gold Price: {min_price:.2f}")

# Log returns
gold["Log_Return"] = np.log(gold["Close"] / gold["Close"].shift(1))

# Annualized volatility
daily_volatility=gold["Log_Return"].std()
annual_volatility=daily_volatility*np.sqrt(252)
print(f"annual volatility Gold Price: {annual_volatility:.2%}")

# Save data
gold.reset_index().to_csv("data/gold_clean.csv", index=False)
print("Data saved successfully!")

# Plot price series
plt.plot(gold.index, gold["Close"])
plt.title("Gold Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.show()

