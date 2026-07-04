# 字典名[键名] -> 字典名.get(key)

# 字典 .keys()  获取所有的键 -> [键,键,键,键]

# 字典 .values()  获取所有的值 -> [值,值,值,值]

# 字典 .items()  1. 获取键值对,把每组封装成元组形式;
#               2. 然后将所有的元组放到一个大列表中
#               3. 即:[(键,值),(键,值),(键,值) ...]


stu_dict = {
    'name': 'zs',
    'age': 20,
    'city': '南京'
}
stu_dict['name'] = 'ww'  # 修改
stu_dict['sex'] = '男'  # 可新增
print(stu_dict.get('age'))

# 字典视图对象一种, 具备遍历 / 可迭代的能力
# print(stu_dict.keys())  # 键
#
# print(stu_dict.values())  # 值            # <class 'dict_keys'>
#
# print(type(stu_dict.keys()))              # <class 'dict_keys'>
#
# print(stu_dict.items(), 'items()')

# print(type(stu_dict.items()), 'items()')  # <class 'dict_items'>
# # 每一项
# newList = stu_dict.items()
# print(newList)  # ([(), (), (), ()])
# print(newList[0])  # # ❌ 注意事项 -> 不支持直接通过下标获取内部的元组项

# 删除
del stu_dict['sex']
# del stu_dict['sex1'] # ❌ 没属性
print(stu_dict)
#
# # 判断键 是否存在
# # 'key' in / 'key' not in
print('name' in stu_dict)  # True
print('age' not in stu_dict)  # False

# 应用题

# 数组对象操作 增删改查 小demo
# 1.创建学生字典
students = [
    {'id': 'S001', 'name': '卢本伟'},
    {'id': 'S002', 'name': '李秀兰'},
    {'id': 'S004', 'name': '赵六'}
]


# 2. 按学号查找姓名
def find_name_by_id(search_id):
    value = input(search_id)
    for stu in students:
        if value == stu['id']:
            return stu['name']
    return "未找到该学生"


search = find_name_by_id('请输入学号:')
print(search)

# 3. 查看所有学号
all_ids = [stu['id'] for stu in students]
print("【3】所有学号：", all_ids)

# 4. 查看所有姓名
all_names = [stu['name'] for stu in students]
print("【4】所有姓名：", all_names)

# 5. 查看完整学号姓名对应
print("\n【5】完整花名册：")
for stu in students:
    print(f"学号：{stu['id']}，姓名：{stu['name']}")

# 6. 增加S005 田七
students.append({'id': 'S005', 'name': '田七'})
print("\n【6】新增学员后：", students)


# 7. 把学号S002学员,改成李小龙
def edit_stu(ids, name):
    value = input(ids)

    for stu in students:
        if value == stu['id']:
            value1 = input(name)
            stu['name'] = value1
            return stu['name']
    return "未找到该学生"


edits = edit_stu("\n【7】请输入id:", '修改这名学生姓名:')
print(edits)
print(students)

# 8. 删除学号S004 赵六

# 不用del

# new_student_list = []
# for stu in students:
#     if stu['id'] != "S004":
#         new_student_list.append(stu)
# students = new_student_list
# print("\n【8】删除S004之后：", students)

# 用 del
# 第一步：找到S004的索引
idx = -1
for i in range(len(students)):
    if students[i]['id'] == 'S004':
        idx = i
        break

# 第二步：判断找到之后，用del按索引删除
if idx != -1:
    del students[idx]

print("\n【8】删除某个", students)

# 纯对象属性操作 小demo
# 1. 创建学生花名册字典 students
students = {
    "S001": "张三",
    "S002": "李四",
    "S003": "王五",
    "S004": "赵六"
}
# 2. 按学号查姓名
search_id = "S002"
print(f"【2】学号{search_id}对应的姓名：{students.get(search_id, '找不到该学生')}")

# 3. 查看所有学号
print("\n【3】所有学号：", list(students.keys()))

# 4. 查看所有姓名
print("\n【4】所有姓名：", list(students.values()))

# 5. 查看完整学号-姓名对应关系
print("\n【5】完整花名册：")
for sid, name in students.items():
    print(sid, name)

# 6. 增加S005学员 田七
students["S005"] = "田七"
print("\n【6】新增S005后花名册：", students)

# 7. S002 修改为李小龙
students["S002"] = "李小龙"
print("\n【7】修改S002后花名册：", students)

# 8. 删除学号S004（赵六）
del students["S004"]
print("\n【8】删除S004后花名册：", students)
