# 三目运算符 / 三元表达式
def max_fn(a, b):
    if a > b:
        return a
    else:
        return b


# 三元公式:
x = 12
y = 11
# 解读: (if x > y) 取 x(左边) 不然的话 取 y(右边)
max_num = x if x > y else y
print(max_num)

# lambda表达式公式
max_num1 = lambda x, y: x if x > y else y
print(max_num1(10, 100))

print('*' * 30)

# 升降序
my_list2 = [3, 1, 2, 4, 5, 56, 6, 7]
my_list2.sort()  # 升序
print(my_list2)

my_list2.sort(reverse=True)  # 降序
print(my_list2)

students = [
    {'name': 'apex', 'age': 18},
    {'name': 'cursor', 'age': 12},
    {'name': 'beach', 'age': 14},
]
# Todo: sort() 排序 -> 基于排序列表中 俩俩比较,不支持 字典 比较
#       列表,sort(key=排序的key索引,reverse = True)
# 方式一:sort + lambda(最直接的升序)
# 1. 按 age 升序比较

students_sort1 = students
# x -> 列表遍历比较过程中 -> 得到一个个字典
students_sort1.sort(key=lambda x: x['age'], reverse=True)
print(students_sort1)
# 结果: apex(18),beach(14),cursor(12)

# 2. 按 name 升序比较
students_sort2 = students
students_sort2.sort(key=lambda x: x['name'])
print(students_sort2)
# 结果: apex, beach, cursor

# 方式二:
