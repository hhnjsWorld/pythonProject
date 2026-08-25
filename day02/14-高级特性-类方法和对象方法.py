# 类方法和对象方法,静态方法
# 类方法
#   类所拥有的方法,通过 @classmethod 修饰
#   特点:
#       第一个参数必须是类对象,通常cls
#       用于访问或操作类属性
#   语法:
#       @classmethod
#       def 类方法名(cls):
#       ...
#       类名.类方法名  # 推荐使用
#       对象名.类方法名
#
# 静态方法:
#   静态方法就像普通的函数,只是放在类里面,
#       用 @staticmethod 修饰
#
#   特点:
#       单纯就是工具函数
#       不需要多定义参数
#   语法:
#       @staticmethod
#       def 静态方法名():
#       ...
#       类名.静态方法名 # 推荐使用
#       对象名.静态方法名

"""
对象方法:
定义:
    def 方法名(self):
使用: 实例对象.方法名() / self.方法名()

类方法
定义:
    @classmethod
    def 方法名(cls): cls -> 类
使用:类名.类方法() / 实例对象.类方法()
----------------------------------
静态方法:
定义:
    @staticmethod
    def 方法名():

使用:类名.静态方法() / 实例对象.静态方法()

"""


class Student:
    holiday_time = 14

    # 类方法
    @classmethod  # 代表着需要加上cls
    def fn1(cls):  # cls 类
        print(cls)
        print(cls.holiday_time)  # 获取当前类的属性

    # 静态方法
    @staticmethod
    def fn2():
        print(Student)
        print(Student.holiday_time)


s = Student()
s.fn1()  # 对象调用类方法
s.fn2()  # 对象调用静态方法

Student.fn1()
Student.fn2()

# 总结:
# self -> 处理具体对象的事情
# @classmethod / @staticmethod -> 处理类的事情
