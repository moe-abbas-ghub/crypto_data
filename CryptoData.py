#!/usr/local/bin/python3
import yfinance as yf
import datetime as dt
import os

# Define the start and end dates
Start = '1900-01-01'  # A very early date to get all historical data
End = dt.datetime.now().strftime('%Y-%m-%d')  # Current date

CryptoList = ['BTC-USD', 'ETH-USD']

# Download data
Crypto_Df = yf.download(CryptoList, start=Start, end=End)['Adj Close']

# Reset index and save to CSV
Crypto_Df = Crypto_Df.reset_index()
Crypto_Df.to_csv(os.getcwd() + "/output_" + dt.datetime.now().strftime("%Y-%m-%dT%H_%M_%S.%fZ") + '.csv', index=False)