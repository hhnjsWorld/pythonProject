t = (1, 2, 3, 4, 5, 6, 6)
# index(元素) -> 返回元素的下标 (索引)
# print(t.index(20))

# count() -> >=0 算出 元素出现次数
print(t.count(6))
print(len(t))

# 元组嵌套
t1 = ((1, 2, 3), (2, 4, 6), (2, 3, 5))
print(t1[1][0])  # 2

# 集合 -> set -> {}
s = {1, 2, 3, 4, 5, 6, 1, 1, 1}
print(s)
print(type(s))  # <class 'set'>

print(30 * "*")

# 应用题
# ① 获取元组的唯一元素(类似于去重), 得到 [1,2,3,4,5,6]

tuple_list = ((1, 2, 3), (2, 4, 6), (2, 3, 5))
# 去重 -> 配合集合 -> 集合 -> 列表
# 创建空集合的方式:
# s = {1,2}
s = set()
print(type(s))
for num_t in tuple_list:
    # print(num_t)
    for num in num_t:
        print(num)
        # 自动做去重动作
        s.add(num)

# 集合
print(s)

# 集合 -> 列表
l = list(s)
print(l)

# 不用set方式:
tuple_list = ((1, 2, 3), (2, 4, 6), (2, 3, 5))
new_list = []

for t in tuple_list:  # 第一层：遍历每个小元组
    for num in t:  # 第二层：遍历元组里的每个数字
        if num in new_list:  # 如果这个数字在新列表里 跳出
            continue
        else:
            # 加进去
            new_list.append(num)  # 就加进去

print(new_list)  # 输出：[1, 2, 3, 4, 6, 5]

# ② 给定一个嵌套元组，里面是三个小组的数学成绩:
scores = ((85, 92, 78, 92), (88, 85, 95, 78), (92, 88, 90, 85))

unique_scores = []  # 存去重后的分数
count_dict = {}  # 存每个分数出现的次数

for group in scores:  # 第一层：遍历每个小组
    for s in group:  # 第二层：遍历小组里的每个分数

        # 去重：不在列表里才加进去
        if s not in unique_scores:
            unique_scores.append(s)

        # 统计次数：每次遇到都 +1
        if s in count_dict:
            count_dict[s] += 1  # 重复 的 数字 出现 了 几次?
        else:
            count_dict[s] = 1  # 要不就出现 1 次

print("去重后的分数：", unique_scores)
print("出现次数：", count_dict)
