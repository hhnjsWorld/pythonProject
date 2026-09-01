# python是一个面向对象的语言, 一切皆对象
# 函数也可以看做是1个对象, 也可以作为参数传递
# 函数名本质上存放的是函数所在空间的内存地址
"""
python中 一切皆对象 包括 元组 / 列表 / 字典 / 整数 ... 还包括函数

def fn()
    xxx

fn -> 函数对象 (地址)
fn() -> 会执行函数内部的代码 -> 返回的结果 return 指定结果

"""


def greet():
    # print('hw')
    return 'hw'


print(greet())  # 上面函数 return 输出为值 / 里是print 无输出 会有None
print(greet)  # 函数名 = 函数对象 -> 地址


# 充当对象,可以赋值
def greet(name):
    return f'Hello, {name}'


# 将函数名赋值给另一个变量
greet_func = greet

print(greet_func('Alice'))
print(greet('Bob'))

# 检查它们是否是同一个对象
print(greet_func is greet)  # True
# id检查是否相同
print(id(greet_func) == id(greet))  # True


# 充当实参,可以传入函数
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculate(operator, a, b):
    """operator参数接收一个函数"""
    return operator(a, b)


# 使用不同的函数作为参数 使用 某 函数对象 进行操作
res1 = calculate(add, 5, 3)
res2 = calculate(multiply, 5, 3)

print(res1)
print(res2)

print('*' * 30)


def greet_fn():
    # print('hw')
    return 'hw'


print(greet_fn())  # 上面函数 return 输出为值 / 里是print 无输出 会有None
print(greet_fn, '地址')  # 函数名 = 函数对象 -> 地址


def my_fn(fn_name):
    print('获取的函数名 or 函数的返回值', fn_name)
    res = fn_name()  # 调用外部传入进来的函数对象
    print(res)


# 将greet函数对象传递给了 my_fn 函数
#   目的: 将来可以在my_fn的内部去调用greet函数
my_fn(greet_fn)

# my_fn(greet_fn())
