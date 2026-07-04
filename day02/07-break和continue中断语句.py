# 应用题
# ① 吃包子 5个包子 -> 吃3个 后面不吃了
i = 1
while i <= 5:
    if i == 4:
        break  # 种植整个循环
    print(f'吃了第{i}个包子')
    i += 1


# ② 吃橘子 -> 第三个坏掉了, 不吃这个,后面的继续吃
# 改进版：吃橘子，第4个坏掉了，只能输入1-5，超过5要提示

def get_eat_orange(num):
    while True:
        try:
            value = int(input(num))

            # 限制范围
            if value > 5:
                print('❌ 一共只有5个橘子，不能超过5')
                continue

            if value <= 0:
                print('❌ 橘子编号必须大于0')
                continue

            # 坏橘子
            if value == 4:
                print('第四个橘子坏了，不吃')
                continue

            print(f'吃第{value}个橘子')

            # 吃到第5个结束
            if value == 5:
                print('橘子吃完了')
                break

        except ValueError:
            print('❌ 请输入数字')


get_eat_orange('吃到第几个橘子:')

# 简版
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(f'吃了第{i}个橘子')
    i += 1

# ③ while 循环实现 1~20 数字的求和,要求跳过 3 的倍数
i = 1
total = 0

while i <= 20:
    if i % 3 == 0:  # 3的倍数
        i += 1
        continue  # 跳过
    total += i
    i += 1

print(total)  # 147

# ④ while 循环实现 1~20 数字的求和,遇到 7 就结束循环
# 推荐写法1
i = 1
total = 0
while i <= 20:
    if i == 7:
        break  # 直接中断，7不加
    total += i
    i += 1

print(total)  # 21

# 写法2
num = 1
total_break_7 = 0

while num <= 20:
    if num % 7 == 0:
        break
    total_break_7 += num
    num += 1

print(f'累加的和{total_break_7}')
