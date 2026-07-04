"""
文件打开模式总览
分为两大类：字符形式(文本)、字节形式(二进制)
可以组合使用 +
"""

# ====================== 字符形式（文本模式，支持编码，处理txt文本） ======================
# 1. r  read 只读
#    只能读文件；文件不存在直接报错；不能写内容
#    open("a.txt", mode="r", encoding="utf-8")

# 2. w  write 覆盖写
#    只能写；文件不存在就新建；文件存在，直接清空原有内容，从头写入
#    open("a.txt", mode="w", encoding="utf-8")

# 3. a  append 追加写
#    只能写；文件不存在新建；文件存在，在文件末尾追加内容，不会清空旧内容
#    open("a.txt", mode="a", encoding="utf-8")


# ====================== 字节形式（二进制模式 rb wb ab，不支持编码，图片/视频/音频） ======================
# 1. rb read binary 二进制只读
#    读取图片、视频；返回bytes字节；不能写，文件不存在报错
#    open("1.jpg", mode="rb")

# 2. wb write binary 二进制覆盖写
#    写二进制数据；文件不存在新建；存在就清空覆盖
#    open("copy.jpg", mode="wb")

# 3. ab append binary 二进制追加写
#    二进制末尾追加字节数据
#    open("1.jpg", mode="ab")

# 4. 不支持码表

"""
补充小知识点：
1. 带 b 的模式 rb/wb/ab → 字节模式，**不能写encoding参数**
2. r/w/a 不带b → 文本字符模式，建议带上 encoding="utf-8"，防止中文乱码
3. + 增强模式： r+ 读写；w+读写；a+读写
"""

# ----------------------- 简单示例代码 -----------------------
# # 文本读
# f = open("test.txt", "r", encoding="utf-8")
# content = f.read()
# f.close()

# # 二进制读图片
# f = open("demo.jpg", "rb")
# data = f.read()
# f.close()

# # 1. 打开文件 - 指定模式 r w a
# # 如果文本文件,指定编码格式
# # f = open('./data/test.txt', 'w', encoding='utf-8') # 写入文字 关闭前无效
# f = open('./data/test.txt', 'a', encoding='utf-8')  # 追加文字 关闭前有效 重启一次追加一次
#
# # 2. 文件操作
# f.write('\nhello 阳阳\n巴巴\n麻麻')
#
# # 3.关闭文件
# f.close()

# 读取
f = open('./data/test.txt', 'r')
# 一般是1024的整数倍
print(f.read(1024))
print(f.read(1024))

f.close()
"""
举例:
    转换为utf-8编码的字节
    text = '你好'
    binary_data = text.encode('utf-8')
    print(binary_data)
    print(len(text))
    print(len(binary_data))
"""

# 字节 -> 计算机认识 (二进制数据)
# 字符 -> 人类认识
# encode -> 字符 -> 字节
text = '你好啊'
#   转成 utf-8 字节
#   1 字符 = 3 字节,以下打印 就是 9个\
print(text.encode()) # b'\xe4\xbd\xa0\xe5\xa5\xbd\xe5\x95\x8a'
print(len(text.encode())) # 9

# 字节 -> 字符 -> decode()
#  '你好啊' 转 字节 后 再 转回 字符
print(text.encode().decode()) # 你好啊