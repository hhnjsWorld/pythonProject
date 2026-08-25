# 见脑图-魔法方法

class Car:
    # 属性跟着 self  表示这些属性是对象的属性
    def __init__(self, color='青色', brand='', number=''):
        self.color = color
        self.brand = brand
        self.number = number

    def run(self):
        print(f'{self}🚗会跑')

    def showCarInfo(self):
        print(f'{self}汽车 = 颜色是{self.color},品牌是{self.brand},轮子数量是{self.number}')


# 需求: 车创建的时候, 给他添加一些通用的属性 颜色 / 轮子 / 品牌...
c1 = Car('绿色', '奔驰', 1)
c1.run()
c1.showCarInfo()
print(f'车的颜色 {c1.color},车的品牌 {c1.brand}')

c2 = Car('紫色', '奥迪', 2)
c2.run()
c2.showCarInfo()
print(f'车的颜色 {c2.color},车的品牌 {c2.brand}')

# 因为我给默认值了,所以创建对象的时候,可以不传参数
c3 = Car()
print(f"车的颜色:{c3.color}")
