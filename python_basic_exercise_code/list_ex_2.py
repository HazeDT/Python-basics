a=[1,2,3,0,4,5]
a.append(10)#附加值
a.insert(1,9)#按序号插入某值
a.remove(2)#移除某值
print(a)
print(a[0])#打印第一位数，对于Python为0
print(a[-1])#打印最后一位
print(a[0:3])#打印前三位0，1，2
print(a.index(3))#打印某值的索引
print(a.count(3))#打印某值出现的次数
a.sort()#从小到大排序
print(a)
a.sort(reverse=True)#大到小排序
print(a)