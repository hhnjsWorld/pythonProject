# 应用题
# ① 猜数字游戏
import random

answer = random.randint(1, 100)
print(f'中标数字为: {answer}')

while True:
    # 获取用户所输入的数字
    guess = int(input('请输入你猜的数字(1~100):'))
    # 判断结果对比
    if guess > answer:
        print('猜大了 请再尝试')
    elif guess < answer:
        print('猜小了 请再尝试')
    else:
        print(f'猜对了!正确答案是: {answer} ')
        break
