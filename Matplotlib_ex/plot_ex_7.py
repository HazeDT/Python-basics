import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-3,3,50)
y1=0.1*x

plt.figure(figsize=(5,5))#figsize设置图片的大小
plt.plot(x,y1,linewidth=10)#scatter表示撒点图
plt.ylim(-2,2)
#gca='get current axis'
ax=plt.gca()
ax.spines['right'].set_color('none')#对应图片的四个边框，这里取消上边框和右边框
ax.spines['top'].set_color('none')
#改变坐标轴的位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines["bottom"].set_position(('data',0))    #outward,axes表示要定位到多少位置
ax.spines["left"].set_position(('data',0))

for label in ax.get_xticklabels()+ax.get_yticklabels():#让曲线不遮挡其他线条
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.7))       #设置图片边框,alpha设置透明度

plt.show()