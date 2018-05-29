import matplotlib.pyplot as plt 
import numpy as np 

x=np.arange(0,10,0.1)
y1=0.05*x**2
y2=-1*y1


fig,ax1=plt.subplots()#定义一个subplot传出数据fig和线条ax1
ax2=ax1.twinx()#将y1的ax1的y轴镜面到另一侧并赋值给ax2
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color='g')
ax2.set_ylabel('Y2',color='b')

plt.show()