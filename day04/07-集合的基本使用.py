# 自练习
# 列表
# [1,2,3]
# 元组
# (1,2,3,4)
# print(type((1,)))
# 字典
# {'键':值}
# 集合
# {1,2,3,4}

# 空集合 / 有数据的集合 -> 关系着 这个集合中 可以去重 能力单一 只负责去重
# 空
s = set()
s1 = {1, 2, 3, 4, 5, 1, 2, 3}
print(type(s))
print(type(s1))
print(s1)  # {1, 2, 3, 4, 5}

# add() 只能添一个参
s1.add(6)
# remove()
s1.remove(1)
print(1 in s1)  # False
print(s1)

# 应用题
# ①
l = ['苹果', '梨子', '菠萝', '香蕉', '香蕉', '苹果']
# 1.定义新列表 -> 遍历原列表 -> 判断列表中的每一项是否存在于列表当中 -> 不存在 -> 添加到列表当中
# 2.配合set()
print(set(l))  # 集合
print(list(set(l)))  # 列表

# ② 从用户评论中提取所有不重复的标签
comment_tags = ['python', '编程', '学习', 'python', '代码', '学习', '算法']
print(list(set(comment_tags)))

# ③
# 1.用户具备读写权限
permissions = {'read', 'write'}

# 2.给用户继续添加 add 和 delete 的权限
permissions = list(permissions)
permissions.extend(['add', 'delete'])
permissions = set(permissions)
print(permissions)

# 3.删除write权限
permissions.remove('write')
print(permissions)

# 判断用户是否有add的权限
print('add' in permissions)