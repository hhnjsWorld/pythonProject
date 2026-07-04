str1 = "yeah hello python hello python hello linux"

# print(str1.内置函数(可选的参数))
# print(str1.find("查找的字符串","起始位置"))

# 找到 为索引13 出现了 重复的hello 查找目标位为下一个重复的是哪个位置
print(str1.find("hello", 15))

# 找不到为-1
print(str1.find("hello1", 15))

# index方法这里为报错
# Todo 后面会讲解 抛出异常问题 -> 不影响后续代码执行
try:
    print(str1.index("hello1", 0))
except ValueError:
    print('查找hello 没找到')

# 应用题
# ① "我认为人工智能必然是未来的方向。人工智能将改变世界。人工智能很重要"
# 问题1:找出"人工智能"这个词第一次出现的位置,用于分析文章重点
text = "我认为人工智能必然是未来的方向。人工智能将改变世界。人工智能很重要"
print(text.find("人工智能", 0))

# 问题2:找出"人工智能"这个词出现的所有位置,用于分析文章重点
print(30 * "-")

# for循环实现
word = "人工智能"
word_len = len(word)
print(range(len(text)))
for i in range(len(text)):
    # print(text[i:i+word_len])
    cut_str = text[i:i + word_len]
    if cut_str == word:
        print("for循环计算'人工智能'位置:", i)

print(30 * "-")

# while方法实现一
keyword = "人工智能"
start = 0
while True:
    pos = text.find(keyword, start)
    # print(pos, 'pospos')
    if pos == -1:
        break
    print("while方法计算出'人工智能'位置", pos)

    start = pos + 1
print(30 * "*")

# while方法实现二
keyword = "人工智能"
start = 0
# 用字符串拼接记录位置
pos_str = ""

while True:
    pos = text.find(keyword, start)
    if pos == -1:
        break
    # 拼接位置字符串
    pos_str = pos_str + str(pos) + " "
    start = pos + 1
print("'人工智能'全部出现位置：", pos_str)
print(30 * "-")

# ② 电子邮箱是 username@example.com
# 提取出你的用户名 username 和 域名 example.com
email = "username@example.com"
# print(email.index('@', 0))
print(email[:8])
print(email[9:])
