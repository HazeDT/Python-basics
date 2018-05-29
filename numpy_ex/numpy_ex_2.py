import numpy as np
a=np.array([10,20,30,40])
b=np.arange(4)
print(a)
print(b)

c=a-b
print(c)

d=10*np.sin(a)#输出a的sin值的10倍
print(d)

print(b<3)#判断b中小于3的数

e=np.array([[1,1],
           [0,1]])
f=np.arange(4).reshape((2,2))
print('\n',e)
print('\n',f)

ee=e*f#二维矩阵相乘为矩阵中各个元素逐个相乘
ff=np.dot(e,f)#二维矩阵相乘为行乘列（线性代数中的矩阵乘法）
ff2=e.dot(f)#点乘
print('\n',ee)
print('\n',ff)
print('\n',ff2)