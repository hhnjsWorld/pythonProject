# 步骤
#   0.在当前目录写入一个工具类 my_sum.py
#   1.全部导入

import my_sum

#
print(my_sum.add1(10, 20))
print(my_sum.add2(10, 20, 30))

#   2.选取某个 方法 再 导入
# from my_sum import add1
#
# print(add1(10, 20))


# 每个模块.py结尾的文件都有一个内置变量 __name__
#   针对于当前模块而言,__name__ == main
#   我在封装的工具类里做了 "if __name__ == '__main__'" 的处理
#       所以 其他人 看不到 我的测试代码 , 仅看到用工具后的运行结果
print('当前的模块 -- 10.文件', __name__)


# -*- coding: utf-8 -*-
"""
=====================================================================
                    Python 内置模块 和 自定义模块
=====================================================================

一、什么是模块？
    模块(Module)就是一个 Python 文件（以 .py 为后缀）
    这个文件里包含了一组相关的函数、变量、类等

二、模块的作用：
    1. 代码复用 —— 写好的函数所有项目都可以直接"拿来就用"
    2. 避免命名冲突 —— 不同模块里可以有同名函数，通过 模块名.函数名() 区分
    3. 逻辑清晰，易于维护 —— 按功能划分到不同模块（database.py / user_info.py）

三、模块的三大来源：
    1. 内置模块  —— Python 自带的，直接 import 就能用（random, os, math, time...）
    2. 自定义模块 —— 自己创建的 .py 文件
    3. 第三方模块 —— 别人开发好的模块，需要 pip install 安装（如 requests, flask）
=====================================================================
"""


# =====================================================================
# 一、内置模块（Python自带，直接import就能用）
# =====================================================================

# ---------- 1. import 模块名（导入整个模块）----------
# 理解：导入一个工具箱，里面有很多工具
# 调用方式：模块名.功能名()

import random
# random 模块：生成随机数
print(random.randint(1, 100))       # 随机整数 1~100
print(random.choice(["苹果", "香蕉", "橘子"]))  # 随机选一个

import math
# math 模块：数学计算
print(math.pi)                      # 圆周率 3.1415926...
print(math.sqrt(16))                # 平方根 4.0
print(math.ceil(3.2))               # 向上取整 4
print(math.floor(3.9))              # 向下取整 3

import time
# time 模块：时间相关
print(time.time())                  # 当前时间戳
# time.sleep(1)                     # 暂停1秒（注释掉，不想等）
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 格式化当前时间

import os
# os 模块：操作系统相关（文件/文件夹/路径）
print(os.getcwd())                  # 获取当前工作目录
print(os.listdir("."))              # 列出当前目录下的文件
# os.mkdir("test_folder")           # 创建文件夹
# os.rename("旧名", "新名")          # 重命名
# os.remove("文件.txt")              # 删除文件
# os.rmdir("空文件夹")               # 删除空文件夹

import json
# json 模块：JSON数据处理
data = {"name": "张三", "age": 25}
json_str = json.dumps(data, ensure_ascii=False)  # 字典转JSON字符串
print(json_str)
data_back = json.loads(json_str)                 # JSON字符串转字典
print(data_back["name"])


# ---------- 2. import 模块名 as 别名（给模块起个别名）----------
# 理解：给工具箱贴个标签，方便书写
# 调用方式：别名.功能名()

import json as js                   # 给 json 起个别名 js
print(js.dumps({"a": 1}))
# 第三方模块常见别名（需要pip install）：
# import numpy as np
# import pandas as pd


# ---------- 3. from 模块名 import 功能名（只导入需要的功能）----------
# 理解：只从工具箱里拿特定的工具
# 调用方式：直接写功能名()，不用加模块名前缀

from random import randint, choice
print(randint(1, 10))               # 直接用，不用写 random.randint
print(choice(["A", "B", "C"]))

from os import getcwd, listdir
print(getcwd())                     # 直接用，不用写 os.getcwd


# ---------- 4. from 模块名 import *（导入所有内容）----------
# 理解：把工具箱里的工具全倒出来
# 调用方式：直接写功能名()
# 注意：不推荐！容易命名冲突，别人看代码不知道这个功能来自哪个模块
# from random import *


# =====================================================================
# 二、自定义模块（自己创建 .py 文件）
# =====================================================================
"""
自定义模块的步骤：
    1. 创建一个 .py 文件（比如 my_utils.py），在里面写函数、变量
    2. 在另一个文件中导入并使用：
       import my_utils
       或
       from my_utils import 函数名

示例：
    假设有两个文件：
    ├── water_flower.py   （模块A：定义水仙花数函数）
    └── main.py           （模块B：导入并调用）
"""


# =====================================================================
# 三、__name__ 变量（每个Python模块都有的内置变量）
# =====================================================================
"""
__name__ 的值：
    - 当文件被"直接运行"时：__name__ == '__main__'
    - 当文件被"导入"到其他文件时：__name__ == 模块的文件名（不含.py）

作用：
    - 写在 if __name__ == '__main__': 下面的代码，只有直接运行本文件时才执行
    - 被其他文件 import 时，这部分代码不会执行
    - 这样模块里的测试代码就不会在导入时自动运行

编写建议：
    - 所有 Python 脚本都应该以 if __name__ == '__main__': 开头
    - 主程序逻辑放在这个块中
    - 模块功能（函数、类）放在块外
"""
