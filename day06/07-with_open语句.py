# 每次都要考虑关闭 语句体 解决
#   with open('路径','模式','码表') as 别名,
#   open('路径','模式','码表') as 别名
# 特点:
# 语句体执行结束后,with后边定义的变量,会自动被释放

# 代码示例
# 应用题
# ① 数据源文件 a.txt: 好好学习,天天向上。123
#   目的:让这段文字全部反转
#   示例
# a = '12345'
# print(a[-1::-1])

f = open('./data/a.txt', 'w', encoding='utf-8')
f.write('好好学习,\n')
f.write('天天向上。\n')
f.write('123\n')
f.close()  # 写完先关掉

with (open('./data/a.txt', 'r', encoding='utf-8') as src_f1,
      open('./data/b.txt', 'w', encoding='utf-8') as src_f2):
    while True:
        # strip() 去掉首行 空格
        line_data = src_f1.readline().strip()
        if len(line_data) == 0:
            break
        print(line_data, end='')
        src_f2.write(line_data[-1::-1] + '\n')
