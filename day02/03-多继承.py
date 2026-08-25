# 应用题:
# 多继承
#   摊煎饼的老师傅 Xufu, 摸爬滚打多年, 研发了一个精湛的煎饼技术
#   将这套技术传授给他最得意的徒弟 Save
#   徒弟 Save 学会了之后, 想要学习更多的技术
#   于是来到了 龙餐馆 ,学习了更多的厨艺


class Xufu:
    def __init__(self):
        self.name = '徐福'
        self.skill = ' [古法徐福烩饭技术] '

    def make_cake(self):
        return (f'{self.name}运用{self.skill}制作烩饭')


# 餐馆的英文: Restaurant
class Restaurant:
    # pass
    # /
    def __init__(self):
        self.name = '龙餐馆'
        self.skill = ' [更多厨艺技术] '

    def make_cake(self):
        return (f'{self.name}运用{self.skill}制作满汉全席')


# 单继承 -> class Save(Xufu): Save 只继承自 Xufu -> 单继承
# 多继承 -> class Save(Xufu,Restaurant): Save 继承自 Xufu 和 Restaurant(餐馆) -多继承
#   多继承就是一个类同时继承了多个类 例:孩子会继承父亲母亲的方法和属性
#   继承顺序 -> 仅仅原则 -> 先找到自己(看自己身上是否具有这个属性和方法)
#       如没有 -> 找父级 ( 从左到右 )

#       譬如: 没找到 Restaurant 就 显示 Xufu 的结果
class Save(Restaurant, Xufu):

    def me(self, name='赛夫'):
        return name


# 师父的技艺 实例函数
Master = Save().make_cake()
me = Save().me()
print(f'{me}继承了{Master}')

# 徒弟 赛夫 继承餐馆 实例函数
# apprentice = Save()
# apprentice.make_cake()

# 继承是类和类之间的关系 和对象没有任何关系
#   mor机制可以查看继承顺序
#   mro机制 可以查看某个对象, 在调用函数的时候,
#       先找哪个类,
#       再找哪个类...
#   1. __mor__
#   2. mor() 方法
# 自己, 左 -> 右
print(Save.__mro__)
print(Save.mro())
