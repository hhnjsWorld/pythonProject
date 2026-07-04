num1 = 20
num2 = 6
num3 = 5
# //最大整除数
print(f'整数:{num1 // num2}')
print(f'整数:{num1 // num3}')

# %取余数
print(f'取余:{num1 % num2}')
print(f'取余:{num1 % num3}')
# *相乘
print(f'幂指数:{num2 * num3}')
# **多少次放
print(f'幂指数:{num2 ** num3}')

# # 基础题
# # 求梯形的面积
# # 公式: S = (a + b) * h / 2
#
# # 输入上底、下底、高
# a = float(input("请输入上底 a: "))
# b = float(input("请输入下底 b: "))
# h = float(input("请输入高 h: "))
#
# # 计算面积
# s = (a + b) * h / 2

# 输出结果
# print(f"梯形面积 S = {s}")

print('算术题↓')
a = 10
b = 20
# a = a + b
a += b
print(a)

print('应用题↓')


# ① (金额 + 税) / 人数 = 均摊
# from decimal import Decimal, ROUND_DOWN
#
# total_bill = float(input('请输入账单金额:'))
# total_friends = int(input('请输入顾客人数:'))
#
# total_bill_with_tax = total_bill * 1.2
# amount_per_customer = total_bill_with_tax / total_friends
#
# amount_per_customer = Decimal(str(amount_per_customer)).quantize(
#     Decimal('0.01'),
#     rounding=ROUND_DOWN
# )
#
# print(amount_per_customer)

# ② 将N个巧克力分给M个儿童
# chocolate_nums = int(input('请输入巧克力数量:'))
#
# children_nums = int(input('请输入小孩数量:'))
#
# # 每人分得多少计算
# chocolate_per = chocolate_nums // children_nums
#
# # 巧克力剩余计算
# chocolate_Leftovers = chocolate_nums % children_nums
#
# print(f'每人分得 = {chocolate_per} 个')
# print(f'巧克力剩余 = {chocolate_Leftovers} 个')

# def get_positive_int(prompt):
#     """循环获取正整数，直到输入正确为止"""
#     while True:
#         try:
#             value = int(input(prompt))
#             # continue 的作用是 输错 你直接重新来
#             if value < 0:
#                 print('❌ 数量不能为负数，请重新输入')
#                 continue
#             return value
#         except ValueError:
#             print('❌ 请输入有效的整数，请重新输入')
#
#
# # === 主程序 ===
# chocolate_nums = get_positive_int('请输入巧克力数量:')
# children_nums = get_positive_int('请输入小孩数量:')
#
# while children_nums == 0:
#     print('❌ 小孩数量不能为0，请重新输入')
#     children_nums = get_positive_int('请输入小孩数量:')
#
# chocolate_per = chocolate_nums // children_nums
# chocolate_leftovers = chocolate_nums % children_nums
#
# print('每人分得 =', chocolate_per)
# print('巧克力剩余 =', chocolate_leftovers)

# ③ BMI = 体重/身高 的 平方
BMI = weight/height