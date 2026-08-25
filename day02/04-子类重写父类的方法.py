# 应用题:
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


# 子类重写 最终 找的还是 自己
# 重写也叫作覆盖，就是当子类属性或方法与父类的属性或方法名字相同时,
#   从父类继承下来的成员可以重新定义!
#   优先自己
class Save(Restaurant, Xufu):
    def __init__(self):
        self.name = '徒弟赛夫'
        self.skill = ' [独创厨艺] '

    def make_cake(self):
        return f'{self.name}运用了{self.skill} 制作煎饼果子!!!'


#   继承顺序 -> 仅仅原则 -> 先找到自己(看自己身上是否具有这个属性和方法)
#       如没有 -> 找父级 ( 从左到右 )
myself = Save().make_cake()
print(myself)
