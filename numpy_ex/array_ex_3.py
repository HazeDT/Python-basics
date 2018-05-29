import numpy as np 

A=np.arange(12).reshape((3,4))
print(A)

print(np.split(A,3,axis=0))#矩阵分割沿着行方向
print(np.array_split(A,4,axis=0))#矩阵进行不等分割
#矩阵分割的第二种方法
print(np.vsplit(A,3))
print(np.hsplit(A,4))