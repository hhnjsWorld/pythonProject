# 导入
# 1. import 模块名
# import os
#
# # 调用方式
# print(os.getcwd())

# 2. 可以自己起名字
#     导入整个模块
# import os as o
#
# print(o.getcwd())

# 3. from 模块名 import 功能名1, 功能名2
#   导入模块里面的某几个函数
# import math
#
# math.floor

# 以上这样写

# 我用谁,就导入谁
# ceil 向上取整 floor 向下取整
from math import ceil, floor

print(ceil(10.8))
print(ceil(10.1))
print(floor(10.1))

# 4.# 不推荐 以下这样做危险,不推荐
# from 模块名 import *
#   导入了模块中的所有函数 而且 调用该的时候 不需要通过函数名.函数名()
#   -> 直接通过函数名
# from time import *
#
# # 3秒后打印
# sleep(3)
#
# print(time())


# import time
# # time.sleep(3) # sleep()延时器
# print(time.time())
# #   时间戳 -> 从1970年 至今所消耗的秒数
# print(time.time())
