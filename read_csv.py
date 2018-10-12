import pandas as pd

##时间市utc时间
header = ['Date', 'open', 'high', 'low', 'close', 'volume']##可以指定,也可以不指定
df = pd.read_csv("bitmex-BTCUSD-5m-2018-10-12-13-46-28.csv",sep = ',',names = header,index_col=0)


''' 
print(df.index)
print(df.index[-1])
'''

print(df)

 
