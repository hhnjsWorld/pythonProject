# 多态 的三个条件
#   1. 有继承 (定义父类、定义子类,子类继承父类)
#   2.函数重写 (子类从写父类的函数)
#   3.父类引用指向子类对象 (子类对象传给父类对象调用者)

"""
多态: 同样的一个函数, 在不同的场景下, 表现出不同的状态 / 形态
    三个条件
        1. 有继承
        2. 函数重写
        3. 父类引用指向子类的对象

"""


#  应用题
# ①
# 动物案例类
#   1. 定义动物类 speak 函数, 表示: 叫
#   2. 定义狗类, 继承自动物类, 重写 speak方法
#   3. 定义猫猫类, 继承自动物类, 重写 speak方法
#   4. 定义函数 make_noise 接受动物对象, 实现传入什么动物, 就怎么叫


# 没有继承,也没有关系 -> python中伪多态 不严格
class Animal:  # 抽象类
    def __init__(self):
        pass


class Car:  # 这里就没有继承关系
    def speak(self):
        print('滴滴答答滴答滴1')


class Dog(Animal):

    def speak(self):
        print('汪汪!1')


class Cat(Animal):
    def speak(self):
        print('喵!')


# 父类引用指向子类的对象
# 实参 Cat()
# an:Animal = Cat() -> 父类引用指向 子类的对象 Cat()
def make_niose(an: Animal):
    an.speak()


# 函数类型说明
def fn(a: int):  # 这里添了 类型约束
    print('函数被调用', a)
    res = a ** 2
    print('函数被调用', res)


fn(10)  # 只有我满足
# fn('10')
# fn(True)
# fn([])

if __name__ == '__main__':
    # 测试
    c = Cat()
    make_niose(c)

    d = Dog()
    make_niose(d)

    # 测汽车
    car = Car()
    # 类型 约束的道理差不多 这里 提示
    make_niose(car)  # 提示 :应为类型 'Animal'，但实际为 'Car'
