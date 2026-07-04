str1 = '我认为人工智能必然是未来的方向。人工智能将改变世界。人工智能很重要'
# replace不会修改原来字符串
str2 = str1.replace('人工智能', 'AI')
str2 = str1.replace('人工智能', 'AI', 2)
print(str2)

# ⭐字符串 -> 字符(分隔符) -> 列表['aa',xxx]
str3 = 'a|b|c'
print(str3.split('|'))

# 列表 -> 字符串
l = ['a', 'b', 'c']

# '分隔符'.join(列表)
print('/'.join(l))
