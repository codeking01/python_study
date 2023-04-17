# author: code_king
# time: 2023/4/17 10:04
# file: multiThread.py
from threading import Thread, Lock


class MultiThread:
    num = 0
    number = 0

    def __init__(self):
        pass

    # 这个是不上锁的
    @classmethod
    def task(cls, num):
        for i in range(10000):
            cls.num += i
        print(cls.num)

    # 这个是上锁的
    @classmethod
    def lock_task(cls, number):
        # 上锁
        mutex = Lock()
        print(cls.number)
        for i in range(100000):
            try:
                mutex.acquire()
                cls.number += 1
            finally:
                mutex.release()
        print("number:", cls.number)
        return cls.number

    @classmethod
    def multi_thread_test(cls):
        t1 = Thread(target=cls.task, args=(cls.num,))
        t2 = Thread(target=cls.task, args=(cls.num,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return cls.num

    @classmethod
    def multi_thread_test_lock(cls):
        t1 = Thread(target=cls.lock_task, args=(cls.number,))
        t2 = Thread(target=cls.lock_task, args=(cls.number,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        return cls.number


if __name__ == '__main__':
    # nums = MultiThread.multi_thread_test()
    # print(nums)
    num1 = MultiThread.multi_thread_test_lock()
    print(num1)
