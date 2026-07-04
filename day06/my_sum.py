# 封装的模块 为了以后 拿来复用
def add1(a, b):
    res = a + b
    return res


def add2(a, b, c):
    res = a + b + c
    return res


# __main__ 的时候 是 自己运行自己的时候
# __自己的文件名(my_sum)__ 的时候是被别的文件导入的时候
# print('my_sum', __name__)

# 测试 -- 自己看到的 不被别人看到 怎么做?
#   __name__ 可以做到
#       每个 python 模块 .py的文件 都有一个内置变量 __name__
#       当文件被直接运行时: __name__ = "__main__"
#       当文件被导入时: __name__ = 模块的文件名

# 在自己做私有测试代码的时候
# 针对与当前/每一个模块而言, __name__ == main
if __name__ == '__main__':
    # __main__
    print('my_sum',__name__)
    print('测试代码1', add1(10, 1000))
    print('测试代码2', add2(10, 1000, 10000))
