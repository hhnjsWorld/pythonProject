# 应用题
# # 需求1: 拷贝 hand.png -> hand1.png 文件中
# #   1. 打开 hand.png 文件 -> 指定字节模式 rb 模式
# src_f1 = open('./data/hand.png', 'rb')
#
# #   2. 打开 hand.png 文件 -> 自定字节写入 wb 模式 -> 自动创建
# src_f2 = open('./data/hand1.png', 'wb')
#
# #   3. white True 按照一定的长度循环读取
# while True:
#     data_byte = src_f1.read(1024)
#     if len(data_byte) == 0:
#         break
#     #   4. 将读取的二进制数据 -  写入 hand1.png 文件中
#     src_f2.write(data_byte)
#
# #   5.关闭文件 (释放资源)
# src_f1.close()
# src_f2.close()

# 需求2: 拷贝 1.txt -> 2.txt 文件中
# ===== 第一步：创建 1.txt 并写入内容 =====
f = open('./data/1.txt', 'w', encoding='utf-8')
f.write('Hello World\n')
f.write('这是第一行\n')
f.write('这是第二行\n')
f.close()  # 写完先关掉

# ===== 第二步：把 1.txt 拷贝到 2.txt =====
txt_f1 = open('./data/1.txt', 'r', encoding='utf-8')
txt_f2 = open('./data/2.txt', 'w', encoding='utf-8')
# 1. 死循环,一直读取,直至读完
while True:
    # 2. 采用1次读取n个(字节)的方式读取
    data = txt_f1.read(1024)  # 长度一般是1024的整倍数
    # 判断是否读取完毕
    if len(data) == 0:
        break
    # 3. 将读取到的内容写入目的地文件中
    txt_f2.write(data)

txt_f1.close()
txt_f2.close()
