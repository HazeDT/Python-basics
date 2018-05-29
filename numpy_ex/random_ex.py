import numpy as np 
a=np.random.random((2,4))
d=np.sum(a)
c=np.sum(a,axis=1)#a\axis=0在每一行中寻找最大值，axis=1在每一列中寻找最大值
e=np.min(a)
f=np.max(a)

print('\n',a,'\n',c,'\n',d,'\n',e,'\n',f)