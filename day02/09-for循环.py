# while -> 遍历次数 不固定

# for -> 固定 长度

# 应用题
# ① 统计字符串 "banana and apple" 中 字母 "a" 出现的次数

str = "banana and apple"
count = 0  # 统算次数初始值

for i in str:
    if i == 'a':
        count += 1

print(f"a出现的次数为{count}")

# ② 统计空格出现的次数, "Python is a great programming language"
str = "Python is a great programming language yeah"
count = 0

for i in str:
    if i == ' ':
        count += 1

print(f"空格出现的次数为{count}")

# ③ range 包左不包右 意思是 1-100 那就是,range(1,101) == range(1,101,1(这个1指的是步长,跨度的意思))
# 应用题
# ① for循环实现计算 1~100 的偶数和
# print(range(101) == range(0, 101, 1)) # True

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(f"偶数和为: {total}")

# 以上公式 等于

total = 0
for i in range(2, 101, 2):  # 运用好步长值
    total += i
print(f"偶数和为: {total}")

# ② for循环,实现 1~10 的乘积
total = 1
for i in range(1, 11, 1):
    total *= i
print(f" 1~10 乘积为: {total}")

# ③ for循环,实现 10~30 中不能被 7 整除的和
# 用步长=1遍历，配合continue跳过
total = 0
for i in range(10, 31, 1):  # 步长=1，默认就是1，可以省略
    if i % 7 == 0:
        continue
    total += i

print(total)  # 357
