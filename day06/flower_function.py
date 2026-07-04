# def flower_fn(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value not in range(100, 1000):
#                 print('❌ 请输入数字 100 ~ 999')
#                 continue
#             else:
#                 result = 0
#
#                 for i in str(value):
#                     result += int(i) ** 3
#
#                 if value == result:
#                     return (f'✔ 水仙花数字{value}成立')
#                 else:
#                     print(f'❌ 水仙花数字{value}不成立')
#
#
#         except Exception as e:
#             # pass
#             print('❌ 请输入有效的数字！')

# 得结果
def flower_fn1(x, y):
    while True:
        try:

            value1 = int(input(x))

            value2 = int(input(y))

            if (1000 > value1 < 0 or 1000 > value2 < 0):
                print('❌ 区间不对')
                continue
            myList = []
            for num in range(value1, value2):
                h = num // 100
                t = num // 10 % 10
                u = num % 10
                if num == h ** 3 + t ** 3 + u ** 3:
                    myList.append(num)

            if len(myList) == 0:
                return '空的'
            else:
                return f'{value1}和{value2}之间的是{myList}'
        except Exception as e:
            pass


print(__name__)
if __name__ == '__main__':
    print(__name__)
    # res = flower_fn('花数:')
    res = flower_fn1('花数1:', '花数2:')
    print(res)
