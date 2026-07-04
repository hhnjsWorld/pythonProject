import os

print(os.getcwd())  # 工作目录 E:\StudyTOAi\pythonProject\day05
# E:\StudyTOAi\pythonProject\day05\13-文件操作-写入内容.py


# 1. 打开文件 open
#   w写的模式,如果文件不存在,则会自动创建
#   w(写)的模式:如果文件存在,会覆盖写入
#   open(r'文件路径',模式) 可以取消转义

# 2. 写入文件 write -> dest_f.write('内容')

# 3. 关闭文件 close

# 应用题 (详情见 open_WriteAndRead_close.txt 的内容)
# ① 往当前工作空间 / open_WriteAndRead_close.txt -> 写入 hi this is python!
# 往文件写入 -> 文件不存在 (主动创建)
# 读取文件内容 -> 文件不存在 (报错)

# #   1. 打开文件 -> 指定文件操作模式 (写 or 读)
# #       同级别省略./
# f = open('open_WriteAndRead_close.txt', 'w')
#
# #   2. 进行读 or 写 操作
# #       覆盖原来的内容
# f.write('hi python1 ~')
#
# #   3. 关闭文件 否则影响性能
# f.close()

# # ② 往当前工作空间 data目录 里的 2.txt -> 写入 'hi this is relative path'!
# f = open('./data/test.txt', 'w')
# f.write('hi this is relative path')
# f.close()

# ③ 扩展: 往当前工作空间 data目录 里的 2.txt -> 写入 'hi this is relative path'!
f = open('../day04/test.txt','w')
f.write('hi this is relative path')
f.close()

