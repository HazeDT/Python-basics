import matplotlib.pyplot as plt 
import numpy as np 

def f(x,y):
    #the height function
    return(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)#生成等高线网格

#use plt.contourf to filling contours
#X,Y and value for (X,Y) point
plt.contourf(X,Y,f(X,Y),8,alpha=0.5,cmap=plt.cm.hot)#数字8表示将等高线分为几部分,cmp来控制图片的冷暖色调

#use plt.contour to add contour lines
C=plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=0.5)
#adding label:clabel
plt.clabel(C,inline=True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()