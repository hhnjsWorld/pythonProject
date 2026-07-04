# lambda 函数作用
# 前提条件 函数只有一个返回值, 且只有一句代码,可以简化
# 变量 = lambda 函数参数 : 表达式 (函数代码 + return返回值)
# 变量() #调用变量

# lambda 表达式,也可以称之为匿名函数
# lambda 表达式在执行完, 会将结果自动返回
# lambda 表达式可以作为值赋值给变量
# lambda 可以作为实参传递,传入不同的函数,实现不同操作

# 场景一 不带参数
def fn_1():
    return ('hello fn1')


result = fn_1()
print(result)

# 以上等同于↓
fn_1 = lambda: print('hello lambda fn_1')
fn_1()

# 不带参数 -> 有返回值
# 变量 = lambda 参数: 一行代码 # 一行代码 不需要添加return,默认会返回结果
fn_11 = lambda: print('hello fn11')
fn_11()


# 带参数 有返回值
def fn_2(x, y):
    return x + y


print(fn_2(100, 200))

fn_3 = lambda x, y: x + y
print(fn_3(200, 300))

# 带参数 有默认值
# 此处 z 是默认值 可以被赋值替换
fn_4 = lambda x, y, z=100: x + y + z
res1 = fn_4(100, 200)
print(res1)
res2 = fn_4(100, 200, 0)
print(res2)
