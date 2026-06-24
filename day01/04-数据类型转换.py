# int类 - 转整数
print(int(10.1))
print(int('10'))
# 但凡他是字符串小数的话 不输出 只认字符串的 "10"
# print(int('10.1'))
print(int(True))
print(int(False))
# 不能遇到文字
# print(int("张三"))

# float类 - 转小数
print(float(10.8))
print(float("10.5"))

# bool类 - 转判断
print(bool(0))
print(bool(1))
print(bool(True))
print(bool(False))
print(bool('True'))
print(bool('False'))
print(bool(''))

# str - 值转成字符串
print(str(10))
print(type(str(True)))

print("-----------")
# eval类 - 转成该有的值
# 最外端的引号去掉
age = '14'
print(type(eval(age)))

bools = '1.1'
print(type(eval(bools)))

bools = 'True'
print(type(eval(bools)))

nameIs = "哈哈"
print("nameIs")
print(eval("nameIs"))



