# python比较简单 / 比较难搞 ->
#   __name__要不要家 -> 标准而言 最好是加
#   __name__ 不是程序运行的入口,只是我们当前代码的标准
#       建议:
#       所有的文件 / 模块 都应该以 __name__ == '__main__' 开始
#       主程序逻辑 放在 __name__ == '__main__' 内部
#       模块 功能 函数 等 放到外面


#
# print('--hello--')
# print('--python--')
#
# if __name__ == '__main__':
#     print('--你好--')
#
# print('--你不好--')

# 以上代码 建议这么写
# def sayHello():
#     print('hi')

# if __name__ == '__main__':
#     print('--你好--')
#     sayHello()


