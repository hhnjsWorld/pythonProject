# ③ 石头剪刀布(嵌套)
import random

# import 导入 (todo 后期会讲)
# print(random.randint(1, 2))

# 1 代表石头 2代表剪刀 3代表布
# 玩家 pk 电脑

player = int(input("请输入手势:(1:石头 / 2:剪刀 / 3:布) : "))
computer = random.randint(1, 3)
if player == computer:
    print('平局')
elif ((player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1)):
    print(computer,'玩家胜利')

else:
    print(computer,"电脑胜利")