# author: code_king
# time: 2023/4/16 20:50
# file: VarMethodClass.py

class Father:
    # 自己内部类的属性，但是new的时候，会应用这个属性
    count = 0

    # 实例化会取调用
    def __init__(self, age):
        self.name = "张三"
        self.age = age
        self.count += 1

    # 内部类方法
    @classmethod
    def class_method(cls):
        print(cls.count)

    # 静态方法
    @staticmethod
    def static_method():
        print("我是静态方法")

    # 实例方法
    def instance_method(self, age):
        print("我是实例方法")
        print(age + 10)


A = Father(18)
A.class_method()
Father.class_method()
Father.static_method()
A.instance_method(18)
B = Father(18)
B.class_method()
Father.class_method()
Father.static_method()
print(B.count)
