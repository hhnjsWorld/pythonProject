"""
global -> 告诉pyhon解释器 -> 函数内修改全局的变量

nonlocal -> 告诉xxx -> 内部函数修改外部函数的变量

"""

age = 10


def change_age():
    # 1. 局部变量 -> 默认不能够修改全局
    # age = 20  # 我只是局部的

    # 2. 回顾 -> global写法
    global age
    age = 30
    print(f'内部函数修改的age: {age}')


change_age()
print(age)

print('*' * 30)


# 示例:
def fn_outer():
    # 1. 内部函数具备 访问 外部函数的能力

    num = 100

    def fn_inner():
        # num = 300正常,num += 100 不对
        #   尝试修改外部num的变量值
        #   num = num + 100 # ❌ 默认内部函数 不具备修改 外部函数变量的能力
        #   num += 100 # ❌

        # 1. 内部函数具备访问外部函数的能力
        # print(f'内部函数访问到的外部函数num: {num}')

        # 2. 定义局部变量 num /  和外部 num变量 没有任何关系
        # num = 300
        # print(num)

        # 3. 解决以上内部访问外部函数 并且 能 修改 的问题
        nonlocal num
        num += 1000
        print(num)

    return fn_inner


res = fn_outer()
res()
