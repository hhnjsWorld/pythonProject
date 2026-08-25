# 题目：校园外卖店铺系统
# 场景：学校里有各种外卖店，它们有共同属性（店名、评分、起送价），但不同类型的店配送规则和特色服务不一样。
# 要求
# 1. 定义父类 Shop（店铺）
# - 属性：name（店名）、rating（评分，如 4.8）、min_order（起送价，如 15 元）
# - __init__：初始化以上三个属性
# - show_info()：打印店铺基本信息，格式如 【店名】评分：4.8 | 起送价：15元
# - calc_delivery(amount)：根据订单金额计算配送费，通用规则：订单金额 ≥ 20 元免配送费，否则收 3 元
# 2. 定义子类 MilkTeaShop（奶茶店），继承 Shop
# - 扩展属性：specialty（招牌产品，默认值 "珍珠奶茶"）
# - __init__：用 super().__init__() 调用父类初始化，再初始化 specialty
# - 重写 calc_delivery(amount)：奶茶店规则 —— 订单金额 ≥ 15 元免配送费，否则收 2 元（奶茶轻）
# - 扩展方法 make_drink(drink_name)：打印制作流程，如 制作中：珍珠奶茶 → 加冰 → 封口 → 完成！
# - 重写 __str__：返回字符串描述，如 奶茶店「蜜雪冰城」，招牌：珍珠奶茶（这是进阶要求，检验你对魔术方法的理解）
# 3. 定义子类 FruitShop（水果店），继承 Shop
# - 扩展属性：freshness（新鲜度，默认值 "当日新鲜"）
# - __init__：用 super().__init__() 调用父类初始化，再初始化 freshness
# - 重写 calc_delivery(amount)：水果店规则 —— 订单金额 ≥ 30 元免配送费，否则收 5 元（水果重）
# - 扩展方法 cut_plate(fruit_name)：打印切果盘流程，如 切果盘：西瓜 → 去皮 → 切块 → 装盒 → 完成！

# # 创建对象
# milktea = MilkTeaShop("蜜雪冰城", 4.8, 10, "柠檬水")
# fruit = FruitShop("鲜丰水果", 4.6, 20, "当日现切")
#
# # 1. 调用继承的方法
# milktea.show_info()
# fruit.show_info()
#
# # 2. 调用重写的方法（各测两个金额，验证免配送费门槛）
# print(milktea.calc_delivery(12))  # 应该收2元
# print(milktea.calc_delivery(20))  # 应该免配送费
# print(fruit.calc_delivery(25))  # 应该收5元
# print(fruit.calc_delivery(35))  # 应该免配送费
#
# # 3. 调用扩展的方法
# milktea.make_drink("柠檬水")
# fruit.cut_plate("哈密瓜")
#
# # 4. 打印对象本身（测试 __str__）
# print(milktea)


class Shop:
    def __init__(self, specialty='', fruitName=''):
        # 店名
        self.name = '蜜雪冰城'
        # 评分
        self.rating = '4.8'
        # 起送价
        self.min_order = 15
        self.amount = 0
        self.specialty = specialty
        self.fruitName = fruitName

    # def show(self,title):
    #     print(title)

    def show_specialty_info(self):

        print(f'店名-{self.name}-评分-{self.rating}-起送价-{self.min_order}')

    def show_fruit_info(self):
        print(f'\n{self.fruitName}店面')

    def calc_delivery(self, amount=0):
        if self.fruitName:

            if amount < self.min_order + 15:
                print('钱太少了,送不了哦')
            else:
                if amount >= 30:
                    print('水果免配送费')
                else:
                    print(f'水果{amount + 5}')
                print('切果盘：西瓜 → 去皮 → 切块 → 装盒 → 完成！')
        else:
            if amount < self.min_order:
                print('钱太少了,送不了哦')
            else:

                if self.specialty == '珍珠奶茶':

                    if amount >= 15:
                        print('珍珠奶茶免配送费')
                    else:
                        print(f'珍珠奶茶{amount + 2}')
                    print('制作中：珍珠奶茶 → 加冰 → 封口 → 完成！')

                else:

                    if amount >= 20:
                        print('果茶免配送费')
                    else:
                        print(f'果茶{amount + 3}')
                    print('制作中：珍珠奶茶 → 加冰 → 封口 → 完成！')


class MilkTeaShop(Shop):
    def __init__(self, specialty=''):
        super().__init__(specialty)
        self.milkName = '奶茶'
        self.title = '我们的目标是没有坏奶茶!'

    def __str__(self):
        return f'{self.title}'


class FruitShop(Shop):
    def __init__(self):
        super().__init__(self)
        self.fruitName = '水果'
        self.freshness = '当日新鲜'
        self.title = '我们的目标是没有坏水果!'
        # super().show(self)

    def __str__(self):
        return f'{self.title}'


MilkTeaShop().show_specialty_info()
MilkTeaShop('珍珠奶茶').calc_delivery(55)
FruitShop().show_fruit_info()
FruitShop().calc_delivery(15)
# FruitShop().calc_delivery(15)
# FruitShop()
# print(MilkTeaShop())
# MilkTeaShop().make_drink()
