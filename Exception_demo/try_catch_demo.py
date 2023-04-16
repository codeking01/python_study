# author: code_king
# time: 2023/4/16 21:12
# file: try_catch_demo.py
import traceback


class ExceptionTest(Exception):
    def __init__(self):
        pass

    @staticmethod
    def try_catch_test():
        try:
            a = 1 / 0
        except Exception as e:
            print(e)
            # 会打印详细信息
            traceback.print_exc()
        else:
            print("else,没有异常")
        finally:
            print("finally 都会执行")

    def throw_exception(self):
        raise Exception("抛出异常")


if __name__ == '__main__':
    e = ExceptionTest()
    # e.try_catch_test()
    a = 1
    b = 0
    assert a + b != 1, "测试失败"
