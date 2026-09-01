# 函数名作为实参使用
#   本质传递的是地址,传入后简洁调用,此时该函数也称之为回调函数


# 应用题
# ① 模拟计算器,接收规则和两个整数 -> 3个形参
"""
1. 定义函数
1.1 三个参数
1.1.1 1 -> 函数对象 (整数的计算规则  -  /)
1.1.2 2 or 3 整数即可

"""


#       实现:传入什么规则,既执行什么操作

def subtract(a, b):
    return a - b


def excepts(a, b):
    return a / b


def calculate(operation, a, b):
    # operation -> 函数对象
    return operation(a, b)


# res = calculate(subtract(10, 20), 10, 20) ❌  错误写法

res1 = calculate(subtract, 5, 3)
res2 = calculate(excepts, 5, 3)

print(res1, '相减的结果')
print(f'{res2:.3f}', '相除的结果')

# lambda 表达式写法
res3 = calculate(lambda a, b: a - b, 20, 10)
print(res3)
