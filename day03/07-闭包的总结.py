# 闭包实现数据私有化原理:
#   通过创建闭包环境，内部函数对外部函数变量形成引用，使对应内存空间不被释放，实现数据私有化。

# 闭包核心要点:
#   作用是保存外部函数变量；语法需满足嵌套函数、内部函数引用外部函数变量、返回内部函数三个条件。

# nonlocal 关键字作用:
#   用于告知 Python 解释器当前要修改外部函数变量，而非定义局部变量。

# 自写测试:
def outer(name='银行'):
    name1 = name
    deposit = 55555

    def inner(name='建设'):
        print(f'{name}{name1}')
        nonlocal deposit
        deposit = deposit + 500

        def inner_inner(name='农业'):
            print(f'{name}{name1}')
            nonlocal deposit

            deposit = deposit + 500
            return deposit

        return inner_inner

    return inner


outer()  # 银行
outer()()  # 建设银行
outer()()()  # 农业银行

print('*' * 30)

print(outer()()())
