import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

print("現実の株価データをダウンロード中...")
ticker = yf.Ticker('AAPL')
aapl_data = ticker.history(period='4y')

aapl_clean = aapl_data.dropna()
real_prices = aapl_clean['Close'].values 
dates = aapl_clean.index 
days = len(real_prices)
start_price = float(real_prices[0])

np.random.seed(42)


daily_volatility = np.std(np.diff(real_prices)) 
steps = np.random.choice([daily_volatility, -daily_volatility], size=days)
pseudo_prices = start_price + np.cumsum(steps)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(dates, real_prices, color='green', linewidth=1.5)
ax1.set_title("Real Stock Chart (Apple Inc. - AAPL)")
ax1.set_ylabel("Price (USD)")
ax1.grid(True)

# 下段：偽物の株価（タイトルも少し変えておいたよ！）
ax2.plot(dates, pseudo_prices, color='blue', linewidth=1.5)
ax2.set_title("Pseudo Stock Chart (Random Walk - Seed 42)")
ax2.set_ylabel("Price (USD)")
ax2.grid(True)

# x軸の日付をナナメにして見やすくする魔法
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
