# 元组入门
# 存储一些重要信息,不希望被程序内意外修改

# tuple1 = ()
# tuple2 = tuple()
# tuple3 = (10, 20, 30)
# tuple4 = (10,)
# tuple5 = (10)
#
# # tuple
# print(type(tuple1))
# print(type(tuple2))
# print(type(tuple3))
# print(type(tuple4))
# # int
# print(type(tuple5))

# 正常我们用这种就行了 ()
# Todo:如果遍历不能出现重复的情况
t = (10, 20, 30, 10, 20, 40)
print(type(t))  # tuple 类型
print(t)  # tuple 类型

# ❌ ↓ 报错为只能放一个 'int' object is not iterable int类型无法支持被序列化(iterable)
# t1 = tuple(101010)

t2 = tuple([1, 2, 3, 4])  # ✔ [] 可以 (1, 2, 3, 4)
print(t2)

t3 = tuple({1, 2, 3, 4})  # ✔ {} 可以 (1, 2, 3, 4)
print(t3)

t4 = tuple({'name': 'zs', 'age': 20})  # ✔ 字典集获取键值
print(t4)

t5 = tuple('102030')  # 分割出来了↓
print(t5)  # ('1', '0', '2', '0', '3', '0')

t6 = ((1, 2, 3), (2, 4, 6), (2, 3, 5))  # 元组嵌套
print(t6)
