# 单引号嵌套双引号 / 双引号嵌套单引号
# 方式1
stu1 = "I'm a boy"
print(stu1)

# 方式2
stu2 = 'I"m a boy'
print(stu2)

# 方式3
stu3 = 'I\'m a boy'
print(stu3)

# \n黄行 \t空格
# 三引号 换行
str = """
你好
123
456
789
"""
print(str)

# 下标为(0 ~ 数据得长度 减去 - 1)
string = 'huhaining'
print(string[0])

string_len = len(string)
print(f'长度为{string_len}')
print(f'最后一位{string[string_len - 1]}')


