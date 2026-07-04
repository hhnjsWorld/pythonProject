# 读 -  详解
#   1. read(n) n ->  一次读取 n 个字符(不区分中文英文),在 utf-8 的编码模式下
#       1 个字符 = 3 个字节
#       n 不写的话读所有(不建议)

#   2. 写入 -> 文件自动创建 / 读取 -> 文件必须存在
f = open('./data/test1.txt', 'r', encoding='utf-8')
#
# # 不传参数读全部
# # char1 = f.read()
# # print(char1)
# # 读取两个字符
# char2 = f.read(2)
# print(char2)  # 我是
# #  续读
# char3 = f.read(2)
# print(char3)  # 谁是
#
# f.close()

# 应用题
# ① 每次读三个字符/字节,直到读完
# 循环
while True:
    char = f.read(2)
    # 如果没有 返回空字符串
    # if not char:
    if len(char) == 0:
        break
    print('读取的字符:', char)
