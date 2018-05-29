import pandas as pd 
import numpy as np 
df1=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2=pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3=pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

print('\n',df1)
print('\n',df2)
print('\n',df3)

res=pd.concat([df1,df2,df3],axis=0,ignore_index=True)#x=0竖向合并，axis=1横向合并,ignore_index后将重新进行排序
print('\n',res)

#join功能,['inner','outer']
df4=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df5=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print('\n',df4)
print('\n',df5)
res1=pd.concat([df4,df5],join='outer') #直接对齐拼接，没有数据的地方用NaN补齐
print('this is result one:\n',res1)
res2=pd.concat([df4,df5],join='inner',ignore_index=True)#将相同的地方对齐拼接，不相同的地方直接剪切掉
print('this is result two:\n',res2)

#join功能,join_axes
df6=pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df7=pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res=pd.concat([df6,df7],axis=1,join_axes=[df6.index])#使用join_axes=[df6_index]命令后使得只考虑df6名称
print(res)

#append aisx=0竖向增加数据，aisx=1横向增加
res=df1.append([df2,df3],ignore_index=True)
print('\n',res)

s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
res=df1.append(s1,ignore_index=True)
print('\n',res)