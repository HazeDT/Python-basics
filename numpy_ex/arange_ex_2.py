import numpy as np 

A=np.arange(3,15).reshape((3,4))
print(A)
print('\n',A[2])#输出第2行的数

print('\n',A[1][1])#输出位于第一行第一列的数
print('\n',A[1,1])

print('\n',A[2,:])#输出第二行所有数

for row in A:
    print('hang\n',row)#输出行

for column in np.transpose(A):
    print('lie\n',column)#通过转秩的方式输出列

print('\n',A.flatten())#A.flatten()返回一个列表，A.flat是第一个迭代器

for item in A.flat:
    print('\n',item)