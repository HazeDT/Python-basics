import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec

fig=plt.figure()
x=[1,2,3,4,5,6,7]
y=[1,3,4,2,5,8,6]

left,bottom,width,height=0.1,0.1,0.8,0.8  #设置图的上下左右边框留多少

axl=fig.add_axes([left,bottom,width,height])
axl.plot(x,y,'r')#打印大图设置线条设置为红色

axl.set_xlabel('x')#设置标签
axl.set_ylabel('y')
axl.set_title('title')
#加小图方法1
left,bottom,width,height=0.2,0.6,0.25,0.25  #设置图的上下左右边框留多少
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(x,y,'b')#打印大图设置线条设置为红色
ax2.set_xlabel('x')#设置标签
ax2.set_ylabel('y')
ax2.set_title('title inside 1')
#加小图方法2
plt.axes([0.6,0.2,0.25,0.25 ])
plt.plot(y[::-1],x,'g')#将y的值逆序打印，绿色线条
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')


plt.show()