import numpy as np 

A=np.array([1,1,1])
B=np.array([2,2,2])
C=np.vstack((A,B))
print(np.vstack((A,B)))#vertical stack 上下合并
D=np.hstack((A,B))#水平合并
print('\n',D)

print(A.shape,C.shape,D.shape)

print(A.T)#不能把横向的序列变为竖向的序列

E=np.concatenate((A,B,A,B),axis=0)#在行方向对A,B,C,D进行合并
print('\n',E)