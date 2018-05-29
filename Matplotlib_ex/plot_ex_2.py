import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()
plt.plot(x,y1)#第一张图

plt.figure(figsize=(5,5))
plt.plot(x,y2)#第二张图
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')#两条线画一个figure里面
plt.show()