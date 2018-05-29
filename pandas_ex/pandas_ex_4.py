import pandas as pd 
import numpy as np 
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])#创建一个表以dates作为行名称，以colums作为列名称

df.iloc[0,1]=np.nan 
df.iloc[1,2]=np.nan
print(df)
print(df.dropna(axis=0,how='any'))#dropnan函数可以选择按行或者按列删除NaN,how={'any','all'}

print(df.fillna(value=0))#用0来填补缺失值

print(df.isnull())#判断nan的位置是否缺少数据
print(np.any(df.isnull())==True)#判一堆数据里是否有丢失数据

