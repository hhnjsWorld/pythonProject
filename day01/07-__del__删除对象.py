# 见脑图-魔法方法
class Car:

    # 属性跟着 self  表示这些属性是对象的属性
    def __init__(self, color='青色', brand='', number=''):
        self.color = color
        self.brand = brand
        self.number = number

    def run(self):
        print(f'{self} 🚗会跑')

    def __str__(self):
        return f'车的颜色是{self.color},品牌是{self.brand},轮子数量是{self.number}'
    # __del__ 的作用是删除对象时调用, 释放对象占用的资源
    def __del__(self):
        # 执行时机:
        #   1. 手动调用 del 实例对象 / 2. 程序执行结束 (释放资源)
        print(f'调用了删除函数{self}')


# 需求: 车创建的时候, 给他添加一些通用的属性 颜色 / 轮子 / 品牌...
c1 = Car('绿色', '奔驰', 1)
print(c1)

c2 = Car('紫色', '奥迪', 2)
print(c2)

print("*" * 30)

print('程序结束')

del c1  # 主动去删除对象 c1 -> 调用 __del__() 魔法方法

# print(c1) del c1 删除对象 c1 就没必要 print(c1)
