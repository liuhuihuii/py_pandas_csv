import ccxt
import datetime
import time
import math
import pandas as pd


###optimization####

##Const variables###
symbol = str('BTC/USD')
timeframe = str('5m')  ##k线 目前仅支持 1m 5m 1h 1d  
exchange = str('bitmex')
start_date = input('请输入开始日期,格式:yyyy-mm-dd HH:MM:SS: ')


def to_unix_time(timestamp):
    epoch = datetime.datetime.utcfromtimestamp(0)  # start of epoch time
    my_time = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")  # plugin your time object
    delta = my_time - epoch
    return delta.total_seconds() * 1000

# CSV File Name
symbol_out = symbol.replace("/", "")
filename = '{}-{}-{}-{}.csv'.format(exchange, symbol_out, timeframe,datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))


exchange = getattr(ccxt, exchange)()
hist_start_date = int(to_unix_time(start_date))
##Maximum result count is 750. Please use the start & count params to paginate
data = exchange.fetch_ohlcv(symbol, timeframe, since=hist_start_date,limit=750)
header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
df = pd.DataFrame(data, columns=header)
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')
df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')


#Precision

df[['Volume']] = df[['Volume']].astype(int)


# Save it
df.to_csv(filename, index=False,header=False, sep=',')

''' 
with open(filename, 'a') as f:
    header = ['Date', 'open', 'high', 'low', 'close', 'volume']##可以指定,也可以不指定
    df1 = pd.read_csv(filename,sep = ',',names = header,index_col=0)
    start_date = df1.index[-1]


    
    df.to_csv(f, header=False)
''' 
