# 应用题
# ① 数组元素处理
names = [
    ['赵', '钱', '孙'],
    ['朱', '秦', '尤'],
    ['戚', '谢', '邹'],
    ['鲁', '韦', '昌'],
    ['李', '许', '喻']
]

# last_data = []
# # 1.提取末尾字、截断原列表
# for i in range(len(names)):
#     last_data.append(names[i][2])
#     names[i] = names[i][:2]
#
# # 2.拆分last_data并追加
# new1, new2 = last_data[:2], last_data[2:]
# names.extend([new1, new2])
#
# print(names)
#
# print()方法自带换行
# hello	python
# print('hello', end='t')
# print('python')

# ② 通过双重for, 打印 names ,要求每三个才换行
# 方式1:
# count = 0
# for name in names:
#     for i in name:
#         count += 1
#         print(i, end='\t')
#         if count % 3 == 0:
#             print('')

# 方式2:

for name in names:
    for i in range(len(name)):
        print(name[i], end='\t')
        if i % 2 == 0 and i != 0:
            print()
