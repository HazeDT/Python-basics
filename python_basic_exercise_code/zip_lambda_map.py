a=[1,2,3]
b=[4,5,6]
print(zip(a,b))#竖向合并如：1，4合并在一起变成（1，4）
print(list(zip(a,b)))

def fun1(x,y):
    return(x+y)
print(fun1(2,3))

fun2=lambda x,y:x+y#lambda用来代替简单的函数，能书写更少的行数
print(fun2(2,3))

print(map(fun1,[1],[2]))#将一个已知函数和参数一起输入,但是返回值为一个项目，需要使用list
print(list(map(fun1,[1],[2])))
print(list(map(fun1,[1,4],[2,6])))#还可以进行多个参数计算