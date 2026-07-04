age = float(input('请输入学生的年龄:'))
if age >= 18:
    print('成年了 可以上网')

# 1. if else 双分支
age = float(input('请输入学生的年龄:'))
if age >= 18:
    print('成年了 可以上网')
else:
    print('滚出网吧!')

# passed_the_exam = int(input('是否通过考试:'))
# if passed_the_exam >= 60:
#     print('恭喜!考试通过')
#
# whether_speeding = float(input('是否超速:'))
# if whether_speeding >= 120:
#     print('您已经超速!')

# password = input("请输入密码:")
# # not 跟着的条件 条件是布尔类型
# # not password
# # 0 '' -> false / 其他 是true
# # 1.password -> 隐式转换成布尔类型 true
# # 2.not 取反
# if not password:
#     print('密码不能为空')

# def get_is_password(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value == '':
#                 print('❌ 请输入用户密码!')
#                 continue
#
#             return value
#
#         except ValueError:
#             print('❌ 请输入用户密码')
#
#
# speed = get_is_password('请输入密码：')
# print("密码已输入")


# 应用题
# ①
eat_meal = float(input('今天吃什么,我兜里有钱:'))
if eat_meal >= 100:
    print('吃个火锅')
else:
    print('吃个泡面')

# ②
weather = float(input('今天穿什么,今天温度是:'))
if weather >= 30:
    print('穿短袖 + 短裤')
else:
    print('穿短袖 + 长裤')


# 2. if elif else 多分支
# ① 春夏秋冬

def get_is_month(prompt):
    while True:
        try:
            value = int(input(prompt))

            month_true = 0 < value < 13

            if not month_true:
                print('❌ 请输入正常月份')
                continue

                # 列表写法
                # if value in [12, 1, 2]:
            if value == 12 or value == 1 or value == 2:
                season = '冬季'
            elif 3 <= value <= 5:
                season = '春季'
            elif 6 <= value <= 8:
                season = '夏季'
            else:
                season = '秋季'

            print(season)
            return season

        except ValueError:
            print('❌ 请输入月份')
            continue


season = get_is_month('请输入月份：')
print('当前季节是：', season)

# ② 度假

pocket_money = float(input("请输入你的零花钱："))

if pocket_money > 10000:
    print("海南3日度假游")
elif pocket_money > 1000:
    print("迪士尼爽玩1天")
elif pocket_money > 100:
    print("买点零食，公园溜溜")
else:
    print("家里蹲，梦游世界")


# ③ 喝酒

def get_drunk_driving(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ 当前数字不能是负数")
                continue
            if 80 / 100 > value >= 20 / 100:
                drunk = "酒驾了"
            elif value >= 80 / 100:
                drunk = "醉驾了"
            elif value == 0:
                drunk = "没喝"
            else:
                drunk = "喝一点"
            print(drunk)
            return drunk

        except ValueError:
            print('❌ 请输酒精含量')
            continue


alcohol = get_drunk_driving('请输入酒精含量：')
print('当前酒精度是：', alcohol)
