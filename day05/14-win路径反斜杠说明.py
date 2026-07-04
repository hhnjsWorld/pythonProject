# 应用题

# 绝对路径注意的点:
# windows系统 是\ 但是\会报错
#   1. 转成 '\\' 或者 '/'
#   2. 前面加个 r
f = open(r'E:\StudyTOAi\pythonProject\day05\open_WriteAndRead_close2.txt', 'w')
f.write('hi this is Absolute path')
f.close()
