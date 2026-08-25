# 抽象类:
# 抽象类是包含一个就或多个抽象方法的类
#   抽象方法 -> 只有声明没有实现
# class Animal:
#     def speak(self):
#         pass  # 无意义的


# 父类确定有哪些方法,具体由子类来实现

# 为什么要有抽象类
#   举例:空调制造标准 - 制冷 - 制热 - 摆风
#       国家或者行业提出标准后, 不同的厂家各自实现标准的要求

"""
抽象类:
    抽象类是包含一个或者多个抽象方法
    
抽象方法:
    没有方法的方法 方法体是由pass修饰的

"""


# 基类 / 父类 指定标准 只制定标准 逻辑 子类写
class AC:
    def __init__(self):
        self.brand = '格力'

    def cool_wind(self):  # 抽象方法
        pass

    def heat_wind(self):
        pass

    def hr_swing(self):
        pass


# 举例: 格力空调
class Gree(AC):
    def cool_wind(self):  # 抽象方法
        print(f'{self.__class__.__name__}{self.brand}制冷')

    def heat_wind(self):
        print(f'{self.__class__.__name__}{self.brand}制热')

    def hr_swing(self):
        print(f'{self.__class__.__name__}{self.brand}摆风')


# 举例: 小米空调
class Xiaomi(AC):
    def cool_wind(self):  # 抽象方法
        print(f'{self.__class__.__name__}{self.brand}制冷')

    def heat_wind(self):
        print(f'{self.__class__.__name__}{self.brand}制热')

    def hr_swing(self):
        print(f'{self.__class__.__name__}{self.brand}摆风')


if __name__ == '__main__':
    Gree().cool_wind()
    Gree().heat_wind()
    Gree().hr_swing()
    Xiaomi().cool_wind()
    Xiaomi().heat_wind()
    Xiaomi().hr_swing()
