# 执行5次 hello python
# 1.定义变量 -> 初始值 -> 计数器
i = 1
# 2.编写循环条件
while i < 6:
    # 循环5次 i已被循环5次
    # i += 1 这里执行 2-6

    print('hello python', i)
    # 3.更新初始值 / 计数器 下面执行1-5
    i += 1
# while i <=5


# 应用题
# ① while计算1-100 循环 所有数字 的 整数合 , 偶数和 , 乘积
# 计算整数,乘积的初始值:
i = 1
# 计算偶数的初始值:
# i = 2

# 计算整数和,偶数和的初始值
# total = 0
# 计算乘积的初始值
total = 1

while i < 101:
    # 整数合:
    # total += i
    # i += 1

    # print("1 到 100 的整数和是：", total)
    # 偶数合:
    # total += i
    # i += 2
    # print("1 到 100 的偶数和是：", total)

    # 乘积:
    total *= i
    i += 1
print("1 到 100 的乘积是：", total)


# ② 兜里有10个游戏币,循环投入机器,直到兜里没币
def get_spendMoney_total(prompt1, prompt2):
    total = 10
    while total > 0:
        try:

            value = int(input(f"{prompt1}{total}个,{prompt2}几个:"))
            if value > 10:
                print("❌ 你没有足够的硬币投入机器")
                continue

            if value <= 0:
                print("❌ 请输入正确数字")
                continue

                # 扣除硬币
            total -= value
        except ValueError:
            print('❌ 请输入正整数')

    if total <= 0:
        return '你没币了'


coin = get_spendMoney_total('硬币还剩：', '你要投')
print(coin)
