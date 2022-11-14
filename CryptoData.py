#!//usr/local/bin/python3
import pandas_datareader.data as Reader
import datetime as Dt
import os

End = Dt.datetime.now()
Start = Dt.date(End.year - 4, End.month, End.day)

CryptoList = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD']

Crpyto_Df = Reader.get_data_yahoo(CryptoList, Start, End)['Adj Close']

Crpyto_Df = Crpyto_Df.reset_index()

Crpyto_Df.to_csv(os.getcwd() + "/output_" + Dt.datetime.now().strftime("%Y-%m-%dT%H_%M_%S.%fZ") + '.csv', index = False)