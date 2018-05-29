import numpy as np 

a=np.arange(4)
b=a
c=a
d=b
print('former a:\n',a)

b=a.copy()#deepcopy的区别是改变a的值b不会改变

a[0]=4
print('latest a:\n',a)
print('this is b\n',b)
print('this is c\n',c)
