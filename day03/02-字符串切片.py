str1 = "abcdefgh"
print(str1[0])  # 通过下标 获取 "某一个"指定的字符
print(str1[2])  # 通过下标 获取 "某一个"指定的字符

# 切片 -> 获取连续的字符

# 字符串变量[起始索引:结束索引:步长] ⭐

# 字符串值: a  b  c  d  e  f  g  h
# 正向索引: 0  1  2  3  4  5  6  7
# 逆向索引:-8 -7 -6 -5 -4 -3 -2 -1

# 包左不包右边
# 起始索引 不写 -> 0
# 结束索引 不写 -> 字符串长度
# 步长 -> 不写 ->

# 正向索引
print(str1[2:5:1])  # cde
# 同等于:
print(str1[2:5])  # cde

# fgh
str1_len = len(str1)
print(str1_len, 'str1_len')

# fgh
print(str1[5:])

# bdfh
print(str1[1:8:2])
print(str1[1::2])

# adg
print(str1[::3])

# degh
print(str1[3:5] + str1[6:8])  # 输出 degh

# 得到 defgh
print(str1[3:])  # 从3号开始，一直捡到最后
print(str1[3:8])  # 和上面效果一样

# 得到 dfh（d、f、h，隔一个取一个）
print(str1[3::2])

print(30 * '-')
# 逆向索引
# bd
print(str1[-7:-4:2])
print(str1[-7:5:2])

# cde
print(str1[-6:-3:1])

# fed
print(str1[-3:-6:-1])
print(str1[5:2:-1])

# 正逆向的步长: 正方向的为1 逆方向的话就是-1

# 错误情况
# abc 咋写?
print(str1[-8:-5:1])  # √

print(str1[-8:-5:-1])  # ×

# hgfedcba 0-8 [0:8:-1] 直接倒过来!
print(str1[::-1])

# 应用题
# ①截取其中的Python
str2 = "Hello,Python World!"
print(str2[6:12:1])

# ② 截取其中的www.baidu.com
str3 = "http://www.baidu.com"
print(str3[7::1])

# ③ 手机号脱敏处理 138****5678
str4 = '13812345678'
print(str4[:3] + '****' + str4[-4::1])

# ④"report_2024.pdf" 提取后缀名 pdf 和 文件名 report_2024
str5 = 'report_2024.pdf'


print(str5[:-4:1])
# .pdf
print(str5[11:])
print(str5[-4::1])

# pdf
print(str5[-3::1])
