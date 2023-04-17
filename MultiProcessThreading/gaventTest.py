# author: code_king
# time: 2023/4/17 11:25
# file: gaventTest.py
import gevent as gevent
from gevent import monkey

# 打补丁，识别所有耗时操作，便于自动操作
monkey.patch_all()
def my_coroutine(x):
    print("f{x} start")
    gevent.sleep(0.2)
    print("f{x} resumed")


# 创建协程
coroutines = [gevent.spawn(my_coroutine(i)) for i in range(3)]
