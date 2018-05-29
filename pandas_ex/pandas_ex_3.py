import pandas as pd 
import numpy as np 
dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])#创建一个表以dates作为行名称，以colums作为列名称

print(df)

print(df['A'],df.A)#打印第一列·

print(df[:3])#打印0到3行

#select by label:loc(用标签进行打印)
print(df.loc['20130102'])
print(df.loc['20130101',['A','B']])#选择20130101行的A,B两列进行打印

#select by position：iloc(用位置筛选和打印)
print(df.iloc[3:5,1:3])

#mixed slection:ix(混合筛选)
print(df.ix[:3,['A','C']])

#Boolean indexing(进行是或否的筛选，选择大于某值的数进行输出)
print(df)
print(df[df.A>8])

df['F']=np.nan#添加一列新的数据
print('\n',df)
