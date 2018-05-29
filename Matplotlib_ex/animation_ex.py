import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation

fig,ax=plt.subplots()#创建一个图片并返回ax

x=np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))#打印图片
i=np.linspace(1,100,100)

def animat(i):
    line.set_ydata(np.sin(x+i/100))
    return line, #逗号表示line返回值为列表，选择第一位需要打逗号

def init():
    line.set_ydata(np.sin(x))
    return line, #逗号表示line返回值为列表，选择第一位需要打逗号


ani=animation.FuncAnimation(fig=fig,func=animat,frames=100,init_func=init,interval=20,blit=False)
#动画长度100帧，更新频率20ms一次，blit表示是否需要更新整张图片
plt.show()