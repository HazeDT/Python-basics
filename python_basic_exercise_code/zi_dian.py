d={'apple':[1,2,3],'pear':1,'orange':{1:3,3:'a'}}#字典用花括号
print(d['apple'])
print(d['orange'][3])
del d['pear']#删除字典中的某个元素
print(d)
d['d']=20#增加字典元素
print(d)