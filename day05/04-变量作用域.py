# 变量作用域
#   一、概述 变量的作用范围
#           1. 变量在哪里可以用
#           2. 变量在哪里不能用

#   二、分类 全局作用域
#           1. 在模块最外层定义
#           2. 在整个模块中都可以访问
#           3. 程序运行期间一直存在

#           局部作用域
#           1. 在函数内部定义
#           2. 只能在函数内部访问
#           3. 函数执行结束后销毁

my_num = 1


# 场景一
def fn():
    """局部 作用域 -> 智能在函数内部使用"""
    my_num1 = 100
    print(f'全局 -> {my_num}')
    print(f'局部 -> {my_num1}')


fn()

# print(my_num1)  # ❌ 找不到 函数内部定义的变量 智能在该局部 访问

# 场景二
num = 1


def fn():
    """局部 作用域 -> 智能在函数内部使用"""
    num = 11
    print(f'局部 -> {num}')


fn()
print(f'我只认全局的(函数外) -> {num}')

# 场景三
# 需求: 在函数内部加工 -> 修改

nums = [1, 3, 5, 7, 7]


def fn():
    # 去重 转回 列表
    nums_list = list(set(nums))  # 先把集合转成列表
    # print(nums_list)

    result = {}

    for i in range(len(nums_list)):
        result[i] = nums_list[i]  # 列表可以通过索引取值
    print(f'函数体加工,索引为key,集合的值为value -> {result}')
    return result


fn()

# 场景四
person = '淑芬'


def name():
    """修改全局变量 global"""
    global person
    person = '村花'
    return person


# global 改变后的全局变量为
nameIs = name()
# 函数体转的
print(nameIs)  # 村花
# 利用global全局也被转成新的
print(person)  # 村花
