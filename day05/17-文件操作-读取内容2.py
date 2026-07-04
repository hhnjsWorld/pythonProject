# 写入 -> 文件自动创建 / 读取 -> 文件必须存在
f = open('./data/gushi.txt', 'r', encoding='utf-8')
# # 1. readline:读取单行
# #       end = '' -> 禁止用print的\n  end = '' 即可解决
# print(f.readline(), end='')
# print(f.readline(), end='')
#
# # 2. readlines:读取多行
# print(f.readlines())
#
# f.close()

# 应用题
# ① readline 读取 gushi.txt 所有行
while True:
    line = f.readline()
    # 理解下这个len : 读不到那一行的长度为止
    if len(line) == 0:
        break
    print(line, end='')
