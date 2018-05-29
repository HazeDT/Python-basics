import matplotlib.pyplot as plt 
import numpy as np

x=np.linspace(-3,3,50)
y1=2*x+1

plt.figure(figsize=(5,5))#figsize设置图片的大小
plt.plot(x,y1)#scatter表示撒点图

#gca='get current axis'
ax=plt.gca()
ax.spines['right'].set_color('none')#对应图片的四个边框，这里取消上边框和右边框
ax.spines['top'].set_color('none')
#改变坐标轴的位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines["bottom"].set_position(('data',0))    #outward,axes表示要定位到多少位置
ax.spines["left"].set_position(('data',0))

#在图上添加一个点
x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b')#s表示点的粗细
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)#画出所描点所对应的虚线

#标注点的名称 method 1

plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
            fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2') )   
#arrowprops生产箭头将需要表明的字指向 图上的点   
#xytext规定需要表明的文字的大小

#method 2
plt.text(-3.7,3,r'$this\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',fontdict={'size':10,'color':'r'})

plt.show()