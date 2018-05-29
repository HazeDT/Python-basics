import matplotlib.pyplot as plt 
import numpy as np 

n=1024
X=np.random.normal(0,1,n) #分别生成x，y方向的随机坐标
Y=np.random.normal(0,1,n)
T=np.arctan2(Y,X)   #将数值的颜色调整的好看
plt.scatter(X,Y,s=75,c=T,alpha=0.5)#生成散点图
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

plt.xticks(())  #隐藏x，y方向的坐标
plt.yticks(())

plt.show()