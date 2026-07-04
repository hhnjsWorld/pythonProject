fruit_names = ['苹果', '橘子', '榴莲', '香蕉', '猕猴桃']
# 遍历
for name in fruit_names:
    print(name)

# range 量长度
for i in range(len(fruit_names)):
    print(i)  # 下标
    print(fruit_names[i])  # 下标所对应

# while 实现
i = 0
while i < len(fruit_names):
    print(i)
    i += 1

# 应用题
# ① 求平均分 -> 成绩总和 / 学生数
score_list = [100, 80, 70, 60, 55, 40]
total = 0
for score in score_list:
    total += score
print(total)
print(f"学生的平均成绩{(total / len(score_list)):.2f}")

# ② 筛数字
price_list = [100, 200, 1000, 4000, 3500]
new_price_list = []

for i in price_list:
    if i < 3000:
        continue
    else:
        # append 这里用append
        new_price_list.append(i)
print(new_price_list)
