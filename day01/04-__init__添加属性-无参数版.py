# 见脑图-魔法方法
# 概述:
#   定义: 给Python类添加魔力的特殊方法
#   特点: 在特殊情况下,会被自动调用
#   写法: __方法名__(),双下划线包围

# __init__(重要)
# 执行时机:
#   创建对象的时候,会自动触发__init__() 魔法方法
class Car:
    def __init__(self):
        print(f'🚗 创建对象时,自动触发 -> 车造好了')

        # __init__ 下能读得出来 -> 属性

        # 自动执行
        print(f'{self} 创建了一个对象')
        # 给所有对象添加属性 - 颜色 / 轮子...
        self.color = '白色'
        self.number = 4

    def run(self):
        print(f'{self}🚗会跑')

    def showCarInfo(self):
        pass


# 需求: 车创建的时候, 给他添加一些通用的属性 颜色 / 轮子 / 品牌...
c1 = Car()
#   可以改值
c1.color = '花色'
c1.number = 8
print(f'c1 车的轮子数量:{c1.number} 车的颜色:{c1.color}')

# 不推荐之前的写法 -> 只关注c1这一辆车而已
# c1.color = '白色'
# c1.wheel = 4

# 推荐写法
c2 = Car()
print(f'c2 车的轮子数量:{c2.number} 车的颜色:{c2.color}')
