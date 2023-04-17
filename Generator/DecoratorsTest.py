# author: code_king
# time: 2023/4/17 12:55
# file: DecoratorsTest.py


def decorate_fun(fun):
    print("outer ,最先执行")

    def inner_fun(*args, **kwargs):
        print("inner 里面 扩展代码")
        print("args", args[0])
        print("kwargs", kwargs.get("age"))
        print("kwargs", kwargs.values())
        fun(*args)

    print("outer ,然后执行")
    return inner_fun


@decorate_fun
def original_fun(num, age=None):
    print("外部方法")


# 在类使用装饰器
class Check(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        print("请先登陆..")
        self.__fn()


@Check
def comment():
    print("我要评论..")


original_fun(55, age=18)
comment()
