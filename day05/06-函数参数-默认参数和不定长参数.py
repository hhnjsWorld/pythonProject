# *args -> 接受多个参数 封装成 元组 (1,2,3,4)
# 实参传递 (1,2,3,4,5)

# *args : *代表 n 个不定长度参数, * 后面 就不用写
def make_breakfast(*args):
    for i in args:
        print(i)
    print(f'{type(args)} 类型: {args}')  # tuple 元组类型


make_breakfast('面包片')
make_breakfast('面包片', '蛋黄派')
make_breakfast('面包片', '蛋黄派', '🍞')


# **kwargs 0> 接受多个参数 封装成字典 {'name':'xx'}
def make_dinner(**kwargs):
    print(f'{type(kwargs)} 类型: {kwargs}')  # dict 字典类型
    for k, v in kwargs.items():
        print(k)
        print(v)


make_dinner(name='银耳羹', color='白色', quantity='3杯')
