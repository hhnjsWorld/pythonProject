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

src_f1 = open('./data/a.txt', 'r', encoding='utf-8')
src_f2 = open('./data/b.txt', 'w', encoding='utf-8')

while True:
    # strip() 去掉首行 空格
    line_data = src_f1.readline().strip()
    if len(line_data) == 0:
        break
    print(line_data, end='')
    src_f2.write(line_data[-1::-1] + '\n')

src_f2.close()
src_f1.close()


