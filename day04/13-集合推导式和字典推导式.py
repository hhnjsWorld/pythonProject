# 集合推导式
# 应用题
# ① 生成 -5 ~ 6之间 的 偶数 的平方集合,并去重处理
result = {x ** 2 for x in range(-5, 7)}
print(result)  # set() 类型  {} 自动去重

# ②
text = "hello world python programming"
chars = {char for char in text if char != ' '}  # 去掉空格
print(chars)

# ③ 生成 1 ~ 5之间的数字序列,该数字做键,该数字的平方做值
# x 做键，x**2 做值
result1 = {str(x): x ** 2 for x in range(1, 6)}
print(result)
# 输出：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ④ 姓名和年龄列表,组合成一个字典
name_list = ['蜘蛛侠', '绿巨人', '黑寡妇']
age_list = [38, 28, 18]

hero_dict = {name_list[i]: age_list[i] for i in range(len(name_list))}
print(hero_dict)

# Todo:元组推导式 -> 没有元组推导式的概念 -> 生成器 generator (之后会讲)
t = (i for i in range(10))
print(t)  # <generator object <genexpr> at 0x0000012AFFBDEA40>
# 0x0000012AFFBDEA40 为对象地址

age = 10
print(id(age))
