# 自练习
# 1 ~ 10 的整数
result = [x for x in range(1, 11)]
print(result)

# 48 ~ 100 的 2 的N次平方 的 整数
result1 = [x for x in range(48, 101) if x in [2 ** n for n in range(7)]]
print(result1)

# 列表推导式 -> 优化
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# ① 基本写法
result2 = []
for i in range(3):
    for s in range(3):
        result2.append((i, s))

print(result2)

# ② 推导式优化写法
result3 = [(x, y) for x in range(3) for y in range(3)]
print(result3)

# 生成 2023 ~ 2025年,1月,2月,3月的信息
# [(2023,1),(2023,2),(2023,3)...]
result4 = [(years, month) for years in range(2023, 2026) for month in range(1, 4)]
print(result4)
