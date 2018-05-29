import threading
import time

def thread_job():
    print('T1 starr\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def main():
    added_thread=threading.Thread(target=thread_job,name='T1')#增加一个线程
    added_thread.start()#开始线程运算
    added_thread.join()#要等join及added_thread全部结束后才运行其后的程序
    print('all done\n')

    print(threading.active_count())#计算有多少个激活的线程
    print(threading.enumerate())#查看是哪些个线程
    print(threading.current_thread())#查看现在运行的线程

#if _name_ =='_mian_':
main()
