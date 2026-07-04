# 一篇文章、一段视频、一个可执行程序,都可以被保存为一个文件,并赋予一个文件名

# 操作系统 (Operating System,简称:os) 以文件为单位管路磁盘中的数据
#   .txt .excel .pdf .awi .png .word .py 等

# 分类: 文本文件、视频文件、音频文件、图像文件、可执行文件等多种类别
# 1. 针对与不同类型的文件,有不同的后缀名,例如:.txt .py .java  .png .mp3 .avi
# 2. 文件可以永久存储

# Todo:
#   1. 打开文件  open('文件路径','模式','码表-可选')
#   2. 读写操作  read() / write()
#   3. 关闭文件  close()函数

# 绝对路径
# 举例:
# 邮寄地址:从国家->省->市->街道->门牌号全部写清楚
# 绝对路径1 = 'C:\Users\Administrator\Music'
# 绝对路径2 = 'D:\python到aiagent学习视频\视频档案\第1章\1\lesson1_llm_basics.py'
# 绝对路径3 = '/home/user/project/data.txt'  #Linux/Mac系统

# 相对路径
# 举例:
# 1.相对于当前项目的路径

# "在我旁边的桌子上",需要知道"我在哪里"

# 相对路径 1 = '1.txt'
#   project/1.txt
#   ./1.txt

# 相对路径 2 = 'data/配置.txt'
#   project/data/配置.txt

# 获取当前工作目录
import os

print(os.getcwd())

# 当前文件 12-文件路径说明 和 1.txt 关系 (同级关系)
# 找到1.txt
# 1.绝对路径 (完整的路径 -> 以磁盘盘符开始) -> 获取 -> 右键 复制绝对路径
#   E:\StudyTOAi\pythonProject\day05\12-文件路径说明.py

# 2.相对路径
#   1.txt  ./1.txt

#   找到data -> 2.txt
#   data 或 ./data
#           ./data/2.txt

#   找到day04 -> test.txt
#   上级目录 ../ -> 工作区间 (day04)
#   ../day04/test.txt
