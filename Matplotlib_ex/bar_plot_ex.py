import matplotlib.pyplot as plt 
import numpy as np 

n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')#facecolor用于设置柱状图主体颜色，edgecolor用于设置边框颜色
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

#标注
for x,y in zip(X,Y1):
    #ha:horizontal alignment
    plt.text(x+0.1,y+0.05,'%0.2f'%y,ha='center',va='bottom' )  #标注时x往右移动0.1，y向上移动0.05个单位，且位于每个柱的中心
for x,y in zip(X,Y2):
    #ha:horizontal alignment
    plt.text(x+0.1,-y-0.05,'-%0.2f'%y,ha='center',va='top' )

plt.xlim(-0.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()