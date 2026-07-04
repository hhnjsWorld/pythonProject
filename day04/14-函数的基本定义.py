# 1. 避免重复劳动 Don't Repeat Yourself (不要重复执行)

# 应用题
# ① 5个不同地方 计算圆形的面积
def calculate_round(p):
    while True:
        try:
            num = float(input(p))

            if num >= 0:
                value = num ** 2
                return value
            else:
                print("❌ 没输入对")

        except ValueError:
            print('❌ 没输入对')


result = calculate_round('请输入数字:')
print(result)


# 原理:
# 函数
# def 函数名(形参1,形参2,...)
#   # 函数体 (代码逻辑 / 计算 ...)
#   # 如果将结果返回
#   # return 结果
#   # 如没写 返回 # return None

# 无传参 , 无返回值
def greet():
    """
    desc:打招呼
    :return: None
    """
    print('hello world')


# 调用 只有你调用函数,才会执行函数内部的代码
greet()


# 有传参 , 无返回值
def greet1(e):  # 形参 : 形式上的参数
    """
    desc:打招呼
    :param e:
    :return:
    """
    print(f'hello {e}')


greet1("刘")
greet1("关")
greet1("张")

#
