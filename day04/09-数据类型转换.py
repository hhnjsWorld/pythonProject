# list set tuple dict

# 列表
l = [1, 2, 4, 5, 6, 1, 2, 3]

# 集合
s = {1, 2, 4, 5, 6, 1, 2, 3}

# 元组
t = (1, 2, 4, 5, 6, 1, 2, 3)

# 字典
d = {"name": "陈浩南", "age": 30, "city": "铜锣湾"}

print('转列表list', list(l))
print('转列表list', list(s))
print('转列表list', list(t))
print('转列表list', list(d))  # Todo:dict()类型 转 字典 只保留键 ['name', 'age', 'city']

# 扩展
# 转字典 -> 场景极少
# 列表转元组
lt = [('name', '小明'), ('sex', '男')]
print(lt)

# 列表套列表
llx = [['name', '小明', '聪明'], ['sex', '男', '是']]  # ❌需要两个值
ll = [['name', '小明'], ['sex', '男']]  # √ 需要两个值
print(dict(ll))  # 打印为字典了{'name': '小明', 'sex': '男'}

# key=value ,key=value
print(dict(name="小明", age=20))
