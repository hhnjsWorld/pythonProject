# 概述
# 全程叫做 Oprating System,系统模块,主要定义了 操作 文件,文件夹 路径 等相关的函数

# rename() : 更改文件的名字

# remove() : 删除某个文件

# mkdir() : 创建一个新的文件夹目录

# getcwd() : 获取当前的工作目录

# chdir() : 改变工作目录

# listdir() : 查看当前文件夹的所有子集(文件,文件夹),不包括子级的子级

# rmdir():
#   1. 删除空文件夹
#   2. 文件夹删除补充 (递归删除、慎重!) 不管有多少层,都全都删掉,不建议
#       import shutil
#       shutil.rmtree('data')

import os

# 重命名
# os.rename('./data/3.txt', './data/4.txt')

# 删除
# os.remove('./data/4.txt')

# 创建目录
#   创建目录顺序需要依次创建 先创 /bb 再/bb/cc
# os.mkdir('./data/bb/cc')

# 获取当前的工作目录 -> 相对路径参考的项目目录
# print(os.getcwd())

# 更改工作目录
# os.chdir('../day05')
#
# f = open('test.txt', 'w', encoding='utf-8')
#
# f.write('hello你好啊\n')
#
# f.close()

# 查看当前的子目录
# print(os.listdir())  # ['xxx','xxx',...]

# 删除目录 (空文件夹)
# os.rmdir('./data')  # ❌ 仅删除非空文件,不然报错提示
# os.rmdir('./data/bb/cc')  # 同理 :创建目录顺序应从最后子级 依次删

import shutil

# 递归思想 -> 不关心 目录里有几层子文件 直接删 -> 不断循环 -> 全部干掉 -> 慎用
shutil.rmtree('./data/bb')
