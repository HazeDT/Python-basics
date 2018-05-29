import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig)

#X,Y value

X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)#画网格
R=np.sqrt(X**2+Y**2)

#height value
Z=np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))#生成三维图，rstride,cstride的数值为图像网格的大小即密集程度
ax.contourf(X,Y,Z,zdir='z',offset=-2,camp='rainbow')#生成3维图的等高线映射图，沿z方向映射,压到z=-2这个位置
ax.set_zlim(-2,2)

plt.show()