# 应用题
# ① 编写一个程序来统计缺失的数字并返回它们的总和
# 例如:在列表 [2,5,3,3,7,5,7] 中,,两个极端 (即2和7) 之间确实的数字是4和6
# 需求:求出缺失值 2 ~ 7 之间
# 0.定义set集合(去重)


l = [2, 5, 3, 3, 7, 5, 7]
s = set(l)
print(s)
# 1.求最小值
min_num = min(l)
# 2.求最大值
max_num = max(l)
count = 0
# print(min_num)
# print(max_num)
# 3.整合区间 range(最小 + 1,最大)
for i in range(min_num + 1, max_num):
    # print(i)

    # 涉及到双重for循环 -> 不要出现外层和内层相同的属性 i -> 问题
    if i not in s:
        print(i)
        count += i
# 4.遍历 -> 获取到确实的值 (和去重后的集合比对)
# 5.初始值 count -> 累加的和
print(count)

# def missing_sum(nums):
#     """
#     统计最小值和最大值之间缺失的数字，并返回它们的总和
#     """
#     if not nums or len(nums) < 2:
#         return 0
#
#     low, high = min(nums), max(nums)
#
#     # 完整区间集合 - 已有数字集合 = 缺失数字集合
#     missing = set(range(low, high + 1)) - set(nums)
#
#     return sum(missing)
#
#
# # ========== 测试 ==========
# nums = [2, 5, 3, 3, 7, 5, 7]
#
# result = missing_sum(nums)
# missing_nums = sorted(set(range(min(nums), max(nums) + 1)) - set(nums))
#
# print(f"原始列表: {nums}")
# print(f"区间范围: {min(nums)} ~ {max(nums)}")
# print(f"缺失的数字: {missing_nums}")
# print(f"缺失数字的总和: {result}")
