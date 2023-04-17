# author: code_king
# time: 2023/4/17 11:59
# file: iterTest.py
from collections.abc import Iterator, Iterable

# 普通迭代器，迭代器
print(isinstance("哈哈哈哈", Iterator))
# 可迭代对象
print(isinstance("哈哈哈哈", Iterable))


# list()

class Fibonacci(object):
    def __init__(self, max_num):
        self.num = max_num
        self.cur_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_num < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.cur_num+=1
            return self.a
        else:
            raise StopIteration


a=Fibonacci(5)
isinstance(a,Iterator)
isinstance(a,Iterable)
print(next(a))
print(next(a))
print(next(a))
print(next(a))