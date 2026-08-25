# 应用题
# 很多顾客都希望能吃到徒弟做出的有自己独立品牌的煎饼果子,
#   也有三只松鼠配方技术的煎饼果子味道。
class Td:
    def __init__(self, product):
        self.product = product
        print(f'{self.product}')

    def sell(self):
        return (f'徒弟家的{self.product}出售')


class Szss(Td):
    def __init__(self, product=' [徒弟派煎饼果子] '):
        super().__init__(product)
        self.taste = ' [三只松鼠味道的煎饼果子] '

    def make(self):
        return f'{self.product}{self.taste},两者兼备'

    # def __str__(self):
    #     return f'{self.product}{self.taste},两者兼备'


res = Szss(' [徒弟派煎饼果子改商标了] ')
print(res.make())


# print(res)


# 调用语法
#   xx.1 -> xx.2 顺序看
#       例:1.1 -> 1.2

# 1. super().__init__() 方式获取


# 2. 父类名字.父类方法名(self)
#       精准调用父类身上的方法


# 3. Case1.__init__(self, '传值')


class Case1:
    def __init__(self, mingzi='后妈'):
        self.name = '父亲'
        self.mingzi = mingzi

    # 2.2 利用函数 输出内容
    def show_Case1(self):
        return f'我是{self.name},父辈从 Case2 调 Case1类方法 来的'

    # 1.2 其他类 接受 并输出
    def show_super(self):
        return f'我是{self.mingzi},从 Case2 里写 super().__init__ 传值过来的'


class Case2(Case1):
    def __init__(self, mingzi=''):
        # 1.1 子 利用  super().__init__() 把值丢给其他类
        super().__init__(mingzi)
        self.name = '儿子'

    # 2.1 精准调用父类身上的方法
    def show_fun(self):
        return Case1.show_Case1(self)
        # return self.name

    # 3.1 Case1.__init__(self)
    def show_init(self):
        # 3.2 Case1.__init__(self) 拿值
        Case1.__init__(self)  # 只调用，用来给 self.mingzi 赋值
        return f'我是{self.mingzi},从 Case2 里写 Case1.__init__(self) 传来的'

    def show_class_fun(self):
        # return Case1.show_Case1(self)
        return Case1.show_super(self)


result0 = Case2().show_Case1()  # 调父级方法
result1 = Case2().show_fun()  # 调父级方法

result2 = Case2('后爸').show_super()  # super().__init__() 拿值

result3 = Case2().show_init()

result4 = Case2('太奶').show_class_fun()

print(result0)
print(result1)
print(result2)
print(result3)
print(result4)

# 总结
# 1. 父类名.父类方法名(self)
#       精准访问, 想找哪个父类, 就调哪个父类
#       适用于多继承

# 2. super().父类方法名()
#       super代表当前对象父类的引用
#       super 只能访问最近的那个父类, 有就用, 没有就往后继续查找,
#       不适用于多继承
