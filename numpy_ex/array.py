import numpy as np 

a=np.array([2,2,3],dtype=np.int)
print(a.dtype)
print('\n',a)

b=np.array([[2,2,3],
            [4,5,6]])
print('\n',b)

c=np.zeros((3,4))
print('\n',c)

d=np.ones((2,3),dtype=np.int)
print('\n',d)

e=np.empty((3,4))
print('\n',e)

f=np.arange(10,20,2)
print('\n',f)

g=np.arange(12).reshape((3,4))
print('\n',g)

h=np.linspace(1,10,5)
print('\n',h)

j=np.linspace(1,10,6).reshape((2,3))
print('\n',j)