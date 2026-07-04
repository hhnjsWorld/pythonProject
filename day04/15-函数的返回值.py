# 应用题
# ① 求 两数 之和
def total(a, b):
    while True:
        try:
            value1 = float(input(a))
            value2 = float(input(b))
            return value1 + value2
        except ValueError:
            print('❌')


result = total('请输入第一个数字:', '请输入第二个数字:')
print(result)
