# C继承了B, B继承了A
class Master:
    def __init__(self):
        self.kongfu = '[古法煎饼果子技术]'
        print(self.kongfu)

    def make_cake(self):
        print(f'运用了{self.kongfu} 制作煎饼果子')


class School:
    def __init__(self):
        self.kongfu = '[白马AI煎饼果子技术]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_school_cake(self):
        print(f'白马运用{self.kongfu}制作煎饼果子')


class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[徒弟独创煎饼果子技术]'

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)


class Prentice_Son(Prentice):
    def smoke(self):
        print(f'徒弟烟鬼')

    def __str__(self):
        return f'继承人的能力: {self.kongfu}'


p_son = Prentice_Son()
print(p_son)  # 自己的

p_son.make_cake()  # 他父类的
p_son.make_school_cake()  # 他父类 的 父类
p_son.make_master_cake()  # 他父类 的 父类

# 继承一定不会超过3层 a -> b -> c / 超过的话 会增加维护的成本