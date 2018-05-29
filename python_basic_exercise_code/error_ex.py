try:
    file=open('aaa','r+')
except Exception as message:#将错误信息存储为message
    print('there is no file named aaa')
    response=input('do you want to create a new file:\n')
    if response=='y':
        file=open('aaa','w')
    else:
        pass
else:#与try对应
    file.write('ssss')
file.close()