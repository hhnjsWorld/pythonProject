# 在 python 中,变量的传递都是 "对象引用传递" 一切皆对象
# (不可变 和 可变对象) -> 行为差异很大

# Todo:单值类型 int float bool

# Todo:容器类型 str list tuple dict set

# 引用理解 变量有自己的内存空间,每个空间都有自己的地址 通过id 查看

age = 12

str1 = '123'

l = [1, 2, 3]


def fn():
    print('你好')


print(id(age))
print(id(str1))
print(id(l))
print(id(fn))

# Todo:在不改变地址的情况下,元素值是否可以改变?
#   内存地址一旦固定,其值是可以发生改变
#       list dict set 类型
#   ----
#   内存地址一旦固定,其值就不能发生改变
#       int float bool str tuple 类型


# int 值不可变 -> 将 值 改变 之后,地址一定会发生改变
a = 1
a1 = a

# a = a1 地址值一样的
print(id(a))
print(id(a1))
a2 = a1
print(id(a2))

a3 = a2
print(id(a3))
a3 = a
a3 = 11
print(id(eval('a3')))  # 已经改变

# 值可变 -> 将 值 改变 之后,地址不会发生改变
my_list = [1, 2, 3, 4, 5, 6]

# my_list.append(7) #可变地址还是之前的

my_list1 = [1, 2, 3, 4, 5, 6]
# 以下地址都一致,值发生了变化,是不会影响地址的
print(my_list is my_list1)  # is 判断 地址是否相等 Fasle

print(my_list == my_list1)  # == 判断值是否相等 True
