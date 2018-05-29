import copy
a=[1,2,3]
b=a
print(id(a))#查看索引
print(id(b))

a[1]=22
print(a)
print(id(a))

c=copy.copy(a)#浅复制，a和c的索引不同,但是里面元素的索引相同
print(id(c)==id(a))

e=copy.deepcopy(a)#深度复制，索引全部不相同
print(id(e)==id(a))