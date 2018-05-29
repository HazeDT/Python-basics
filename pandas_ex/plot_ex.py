import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#plot data

#Series
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()
data.plot()
plt.show()
#DataFrame
data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data=data.cumsum()
print(data.head())
#plot methods:'bar','hist','box','kde','area','hexbin','pie'

ax=data.plot.scatter(x='A',y='B',color='DarkBule',label='Class1')
data.plot.scatter(x='A',y='C',color='DarkGreen',label='Class2',ax=ax)#一张图上打印两组数据
plt.show()

