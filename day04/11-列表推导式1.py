# 创建一个0-9的列表
# 回顾
# while
i = 0
l = []
while i < 10:
    l.append(i)
    i += 1
print(l)

# for
l1 = []
l1oushu = []  # 偶数
l1jishu = []  # 奇数
for i in range(10):
    # l1.append(i)
    if i % 2 == 0:
        l1oushu.append(i)
    if i not in l1oushu:
        l1jishu.append(i)
print(l1)
print(l1oushu)
print(l1jishu)

# 记住概念
# Todo:结果 = [表达式 for 变量 in 可迭代对象 if 条件]
# 应用题
# ①
# 创建平方数列表

# 带条件的列表推导式(偶数)

# ②
# 1 ~ 10 之间的整数列表
nums_1_10 = [x for x in range(1, 11)]
print(nums_1_10)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1 ~ 10 中，偶数的平方
squares_even = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squares_even)   # [4, 16, 36, 64, 100]

# 50 ~ 100 之间的偶数列表
evens_50_100 = [x for x in range(50, 101) if x % 2 == 0]
print(evens_50_100)   # [50, 52, 54, ..., 98, 100]


