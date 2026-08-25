# 巩固加深:
# 对象属性和类属性
# ①
# 对象属性:
#   属于各自对象自己, 每个对象都有 [独立] 的一份
#   修改影响:
#       系应该只影响该对象自身
#   定义格式:
#       类外: 独享名.属性名 = 属性值
#       类内 __init__ 中:self.属性名 = 属性值
#   获取格式:
#       对象名.属性名
#       self.属性名

# ②
# 类属性:
#   属于[类本身], 所有对象共享同一份
#   修改影响:
#       修改后, 所有对象和类的访问都受影响
#   调用方式:
#       类名.类属性名(推荐)
#       对象名.类属性名(可以访问到,但不推荐)
class Student:
    holiday_time = 14
    """
        类属性
        类, 对象都可以获取
        推荐: 快

        对象是可以获取,但是不建议,没必要

    """

    """
        self 实例对象 - 谁调用 就指向谁
        name age -> 属于梳理对象本身的,互不影响的

    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'学生的信息: {self.name} - {self.age}'


# 问一: s1 s2 -> 互不影响
s1 = Student('小王', 18)
print(s1)
s2 = Student('小王', 18)
print(s2)

# 问二: 怎么快速拿到类中属性 -> Student.holiday_time
print(s1.holiday_time)
print(s2.holiday_time)
print(Student.holiday_time)

# 问三: 当前如果直接通过类.属性名 进行类属性的修改 -> 影响所有
Student.holiday_time += 2

print(s1.holiday_time)
print(s2.holiday_time)
print(Student.holiday_time)

# 总结:
#   类属性:
#       数据在所有实例间共享且不变时
#       作为默认值
#   对象属性:
#       数据时实例特有的
#       数据会频繁变化
#       需要独立状态管理
