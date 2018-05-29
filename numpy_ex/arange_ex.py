import numpy as np 

A=np.arange(2,14).reshape((3,4))
print('\n',A)
print(np.argmin(A))#求序列A中的最小值的索引即序号
print(np.argmax(A))

print('\n',np.mean(A))#计算序列平均值
print('lie_mean\n',np.mean(A,axis=1))#计算列平均值

print(np.median(A))#计算序列中位数

print(np.cumsum(A))#生成累加序列
print(np.diff(A))#累差生成矩阵

print(np.nonzero(A))#寻找非零数，输出其位置信息

print('\n',np.sort(A))#排序

print('\n',np.transpose(A))#矩阵转秩或者写为(A.T).dot(A)

print(np.clip(A,4,10))#将所有小于4的数变为4，大于10的数变为10

