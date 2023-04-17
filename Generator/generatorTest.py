# author: code_king
# time: 2023/4/17 11:38
# file: generatorTest.py

temp = (i for i in range(5))
for i, j in enumerate(temp):
    print(i, j)


# 使用yield关键字，写一个fibonacci
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    num = fibonacci(10)
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))
