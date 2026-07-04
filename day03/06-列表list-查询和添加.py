# Todo:增删改查

# 查询
l = ['盖伦', '德邦', '皇子', '德莱文', '人马', '皇子']

# index() -> 查找当前索引
print(l.index('德莱文'))  # 3

# count() -> 出现的次数 >= 0
print(l.count('皇子'))  # 2

# in -> 判断是否在列表
print('德邦' in l)  # True
print('阿卡丽' in l)  # False

# append() -> 列表加元素 argument参数 只能追加 1个 元素
l.append('塞恩')  # ✔
print(l)
# l.append('塞恩', '奥恩')  # ❌

# insert() -> 指定位置添加
l.insert(1, '瑞文')
print(l)

# extend() -> 数组合并
l1 = ['卡莉斯塔', '锤石']
# int类型的 2 不是序列化数据 (不可以遍历)
# l.extend(2)  # ❌
l.extend('2')  # ✔
l.extend(l1)  # 自己 加自己
print(l)
