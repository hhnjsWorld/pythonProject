# 字典的遍历
name = {
    'nm1': '张三',
    'nm2': '李四',
    'nm3': '王五'
}

# 获取key
# 写法一
# 直观的获取key
# keys()
for key in name.keys():
    print(key)  # 获取所有的键

# 写法二
for key in name:
    print(key)  # 获取所有的键

# 获取value
# values()
for value in name.values():
    print(value)  # 获取所有的值

# 获取值 和 键
# items()
# 写法一
for item in name.items():
    # Todo 牢记获取到的是元组组成的
    # print(type(item)) # tuple
    print(f'键名为:{item[0]},值为{item[1]}')

# 写法二:直观写法
for key, value in name.items():
    print(f'键名为:{key},值为{value}')

# 应用题
# ① 创建各科目分数字典
subjects = {"数学": 85, "英语": 79, "语文": 100, "物理": 88, "化学": 55}

# ② 获取所有考试的科目,并打印出来
for subject in subjects.keys():
    print(subject)

# ③ 求取学生的平均分
total = 0
score = []
for subject in subjects.values():
    score = subject
    total += score

print(f'总分:{total}')
print(f'总分 / 科目数量 = 平均分:{total / len(subjects)}')

# ④ 打印成绩表,将科目和成绩对应起来 输入格式 数学 的成绩为 100

for subject in subjects.items():
    print(f'科目-{subject[0]}的成绩为:{subject[1]}')

for k, v in subjects.items():
    print(f'科目-{k}的成绩为:{v}')
