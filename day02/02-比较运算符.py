a = 10
b = 20
# =赋值,== 比较
print(a == b)  # F
print(a != b)  # T
print(a >= b)  # F
print(a <= b)  # T

print('应用题↓')

# stu_age = int(input('请输入你的年龄:'))
# result = '是成年' if 10 <= stu_age <= 20 else '不是成年'
# print(f"是否符合青少年的标准:{result}")

# and并在关系写法
stu_age = int(input('请输入你的年龄:'))
# print(f'是否符合青少年标准:{stu_age >= 10 and stu_age <= 20}')
# 同等于写法↓
print(f'是否符合青少年标准:{10 <= stu_age <= 20}')

# or写法或写法
print(f'是否符合青少年标准:{stu_age <= 10 or stu_age >= 80}')

# not取反 非
print(f'是否未成年: {not (stu_age < 18)}')


# ① 高速限速,速度必须保持在60~120之间
def get_speed_int(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 60 or value > 120:
                print('❌ 时速必须保持在60~120km/h之间')
                continue

            return value

        except ValueError:
            print('❌ 请输入有效数字')


speed = get_speed_int('请输入时速：')
print(f'当前时速：{speed}km/h')

# ② 模特选秀,身高必须超过 170 cm,并且体重小于 110 斤

# def get_bodyType_init(prompt1, prompt2):
#     while True:
#         try:
#             height = float(input(prompt1))
#
#             if height < 170:
#                 print('❌ 身高必须超过 170,重写')
#                 continue
#
#             break
#
#         except ValueError:
#             print('❌ 请输入有效数字')
#
#     while True:
#         try:
#             weight = float(input(prompt2))
#
#             if weight >= 110:
#                 print('❌ 体重必须小于 110,重写')
#                 continue
#
#             break
#
#         except ValueError:
#             print('❌ 请输入有效数字')
#
#     return height, weight
#
#
# height, weight = get_bodyType_init('请输入身高:', '请输入体重:')
# print(f'符合要求，身高：{height}cm，体重：{weight}斤')

# def get_bodyType_init():
#     while True:
#         try:
#             print('请输入身高:')
#             print('请输入体重:')
#
#             height = float(input())
#
#             if height <= 170:
#                 print('❌ 身高必须超过170，请重新填写')
#                 continue
#
#             weight = float(input())
#
#             if weight >= 110:
#                 print('❌ 体重必须小于110，请重新填写')
#                 continue
#
#             return height, weight
#
#         except ValueError:
#             print('❌ 请输入有效数字')
#
#
# height, weight = get_bodyType_init()
# print(f'符合要求，身高：{height}cm，体重：{weight}斤')

# # ③ 老家相亲,余额超过10万 或 年纪小于28岁
# def get_Target_init(prompt1, prompt2):
#     while True:
#         try:
#             money = float(input(prompt1))
#
#             if money < 100000:
#                 print('❌ 彩礼不够10万')
#                 continue
#
#             break
#
#         except ValueError:
#             print('❌ 请输入有效数字')
#
#     while True:
#         try:
#             age = int(input(prompt2))
#
#             if age >= 28:
#                 print('❌ 年龄必须小于28岁')
#                 continue
#
#             break
#
#         except ValueError:
#             print('❌ 请输入有效数字')
#
#     return money, age
#
#
# money, age = get_Target_init('输入金钱:', '输入年纪:')
# print(f'符合要求，金额：{money}，年龄：{age}')
