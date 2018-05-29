#merge也是一个合并函数,merging two df by key/keys.(maybe used in database)

import pandas as pd 

left=pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})
right=pd.DataFrame({'key':['K0','K1','K2','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})
print(left)
print(right)

res=pd.merge(left,right,on='key')
print(res)

#consider two keys
left=pd.DataFrame({'key1':['K0','K1','K2','K3'],
                  'key2':['K0','K1','K0','K1'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right=pd.DataFrame({'key1':['K0','K1','K2','K3'],
                   'key2':['K01','K0','K0','K0'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})
res=pd.merge(left,right,on=['key1','key2'])
print('\n',res)

#how=['left','right','outer','inner']共四中用法
res=pd.merge(left,right,on=['key1','key2'],how='inner')
print(res)

#indicator
df1=pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2=pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
re=pd.merge(df1,df2,on='col1',how='outer',indicator=True)
print('1st\n',res)
#give the indicator a custom name
#res=pd.merge(df1,df2,on='col1',how='outer',indicator=_column)
#print('2nd\n',res)


