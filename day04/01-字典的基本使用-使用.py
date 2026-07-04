# 描述学生的信息
# 姓名 / 家乡 / 性别 / 年龄 / 身高

stu_list = ['ls', '北京', '男', '20', '180cm']

# 字典 -> 一组键值对的集合
# key 键 -> 必须是字符串 '' ""
# value 值 -> bool True / int 10 / str "" ''

stu_dict = {
    'name': 'zs',
    'age': 20,
    'city': '上海'
}

stu_dict['age'] = 30
print(stu_dict['age'])

print(stu_dict)

# 空字典  {}   dict()
d = {}
d1 = dict()
print(type(d))
print(type(d1))

# 空集合 set()
print(type(set()))

# 非空集合
print({1,2,3,4})

print(type({1,2,3,4}))
