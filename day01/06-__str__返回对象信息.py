# 见脑图-魔法方法

class Car:
    """
    该init方法用于给对象添加属性
    :param color: 颜色
    :param brand: 品牌
    :param number: 轮子数量
    """

    # 属性跟着 self  表示这些属性是对象的属性
    def __init__(self, color='青色', brand='', number=''):
        self.color = color
        self.brand = brand
        self.number = number

    def run(self):
        print(f'{self}🚗会跑')

    # __str__ 辅助init 出结果, 返回对象的属性
    def __str__(self):
        # 为什么不能直接{self}? 因为self是对象,对象是无法直接返回的,需要返回对象的属性
        # print(f'{self}是一个对象') # ❌ RecursionError: maximum recursion depth exceeded
        # 执行时机, print打印对象的时候, 会自动调用__str__() 魔法方法
        return f'车的颜色是{self.color},品牌是{self.brand},轮子数量是{self.number}'


# 需求: 车创建的时候, 给他添加一些通用的属性 颜色 / 轮子 / 品牌...
# 不要返回对象的地址 0x... ,而是返回对象的属性
c1 = Car('绿色', '奔驰', 1)
print(c1)

c2 = Car('紫色', '奥迪', 2)
print(c2)
