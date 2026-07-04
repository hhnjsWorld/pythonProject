# 应用题
# ① 求一个数组中每对相邻元素的最大值,并收集起来
# 输入:[7,8,9,5,6,7,2,3] -> [8,9,9,6,7,7,3]
original_list = [7, 8, 9, 5, 6, 7, 2, 3]

# 方式1:
new_list = []
for i in range(len(original_list) - 1):
    # print(original_list[i])
    # 比较当前项和下一项
    if original_list[i] > original_list[i + 1]:
        new_list.append(original_list[i])
    else:
        new_list.append(original_list[i + 1])
print(new_list)

# max(当前数,后一个数)
# 方式2:
new_list1 = []

for i in range(len(original_list) - 1):
    current_num = original_list[i]
    next_num = original_list[i + 1]
    # 每次遍历时 -> 获取到的前后最大的那个值
    max_num = max(current_num, next_num)
    # print(max_num)
    new_list1.append(max_num)
print(new_list1)
