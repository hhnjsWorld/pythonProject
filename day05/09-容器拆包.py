# 拆包: 把容器的数据一个一个拆解出来的过程

# 语法:      tuple1 = (10,20)
#           num1,num2 = tuple1
#           a,b = ['菊花','腊梅']


# 把容器的数据一个一个拆解出来的过程
t = (1, 2)
# 取 第一个 + 第二个
fir = t[0]
sec = t[1]
print(fir, sec)

# 拆包 类似 js 解构
f, s = t
print(f, s)

# 列表当中 拆解
my_list = ['刘', '关', '张']
# 拆包
f1, s2, t3 = my_list
print(f1, s2, t3)

# 应用题
# ① 交换两个变量的值
c1 = '可乐'
c2 = '雪碧'

# 方法一 借助第三个变量
temp = c1
c1 = c2
c2 = temp
print(c2, c1)

# 方法二 直接拆包颠倒赋值
c2, c1 = [c1, c2]
print(c1, c2)
