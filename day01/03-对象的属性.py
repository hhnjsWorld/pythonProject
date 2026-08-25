class Car:

    def run(self):
        print(f'{self}🚗会跑')

    def showCarInfo(self):
        self.color = '黑色'
        self.number = 8
        print(f'{self}的颜色是{self.color}, 号码是{self.number}')


# 需求:
# 1. 类的外面添加 - 直接给创建出来的实例对象添加
# ① 外部添加属性
c1 = Car()
c1.color = '白色'
c1.number = 4
print(f'{c1}的颜色是{c1.color}, 号码是{c1.number}')

# 内部添加属性
c1.showCarInfo()

# 2. 类的内部添加 Todo
