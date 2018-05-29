import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure(figsize=(5,5))#figsize设置图片的大小

plt.xlim((-1.2))#设置坐标轴的范围
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks=np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)#将x坐标的数值改为新建立的new_ticks
plt.yticks([-2,-1.8,-1,1.22,3],
           ['$really bad$','bad','normal ','good','really good'])#$来优化字体，能识别反斜杠\+空格，r表示正则表达 

l1,=plt.plot(x,y2,label='up')#label中的up表示图的名字
l2,=plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')#两条线画一个figure里面

plt.legend(handles=[l1,l2],labels=['aa','bb'],loc='best')#打印图历  handles表示将l1，l2表示的线框起来   
##lables表示给l1和l2给定一个新的图历名字来代替以前的
##loc表示图历位置，best表示寻找最佳位置，upper right 表示右上角


plt.show()