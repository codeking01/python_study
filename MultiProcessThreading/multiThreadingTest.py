# author: code_king
# time: 2023/4/17 15:04
# file: multiThreadingTest.py
import ctypes
from threading import Thread

num = 0


def task1():
    global num
    for i in range(10000000):
        num += 1


def task2():
    global num
    for i in range(10000000):
        num -= 1


# 开启多线程
t1 = Thread(target=task1)
t2 = Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print("num:", num)


# python终止线程的方法
def kill_thread(self, inner_work_thread):
    # 终止线程
    async_exc = ctypes.py_object(SystemExit)
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(inner_work_thread.ident), async_exc)
