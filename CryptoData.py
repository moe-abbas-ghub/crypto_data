#!/usr/local/bin/python3
import yfinance as yf
import datetime as dt
import os

End = dt.datetime.now()
Start = dt.date(End.year - 4, End.month, End.day)
CryptoList = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD']

# Download data
Crypto_Df = yf.download(CryptoList, start=Start, end=End)['Adj Close']

# Reset index and save to CSV
Crypto_Df = Crypto_Df.reset_index()
Crypto_Df.to_csv(os.getcwd() + "/output_" + dt.datetime.now().strftime("%Y-%m-%dT%H_%M_%S.%fZ") + '.csv', index=False)