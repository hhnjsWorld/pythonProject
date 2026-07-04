# 应用题
# ① 利用字典 {} , 统计字符串中每个字符的次数
strings = 'aaaaabbccc2131234333'
count_dict = {}
for char in strings:
    if char in count_dict:
        # 字符已经在字典里，次数+1
        count_dict[char] = count_dict[char] + 1
    else:
        # 字符不在字典，初始次数为1
        count_dict[char] = 1

print(count_dict)

