import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(figsize=(5,5))#figsize设置图片的大小
plt.plot(x,y2)#第二张图
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')#两条线画一个figure里面
plt.xlim((-1.2))#设置坐标轴的范围
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)#将x坐标的数值改为新建立的new_ticks
plt.yticks([-2,-1.8,-1,1.22,3],
           ['$really bad$','bad','normal ','good','really good'])#$来优化字体，能识别反斜杠\+空格，r表示正则表达 
#gca='get current axis'
ax=plt.gca()
ax.spines['right'].set_color('none')#对应图片的四个边框，这里取消上边框和右边框
ax.spines['top'].set_color('none')
#改变坐标轴的位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines["bottom"].set_position(('data',0))    #outward,axes表示要定位到多少位置
ax.spines["left"].set_position(('data',0))
plt.show()