# 应用题
# ① 死写法
# 编写一个函数 `group_by_length(words)` , 将单词列表按长度分组
# **调用示例**: `group_by_length(['apple','bat','cat','elephant','dog'])`
# **期望输出**: `{3:['bat','cat','dog'],5:['apple'],8:['elephant']}`
# animals = ['apple', 'bat', 'cat', 'elephant', 'dog']


# def group_by_length(words):
#     # 重排序
#     animals_sort = sorted(words)
#     # 重组
#     l1 = animals_sort[1:4:]
#     l2 = animals_sort[:1:]
#     l3 = animals_sort[-1:-2:-1]
#
#     # for k, v in dicts.items():
#     dicts = {3: l1, 5: l2, 8: l3}
#     return dicts
#
#
# res = group_by_length(animals)
# print(res)


# 练一练
# ① 推导式 写法 最简单!
animals1 = ['apple', 'bat', 'cat', 'elephant', 'dog']
result = [{"name": w} for w in animals1]
print(result)

# ② 循环写法
animals2 = ['apple', 'bat', 'cat', 'elephant', 'dog']


def get_types(l):
    result = []

    for word in l:
        d = {"name": word}  # 每循环一次造一个字典
        result.append(d)

    return result


# [{'name': 'apple'}, {'name': 'bat'}, {'name': 'cat'}, {'name': 'elephant'}, {'name': 'dog'}]


ref = get_types(animals2)
print(ref)


# ② 活写法


def group_by_length(words):
    # 第一步：收集全部长度
    len_list = []
    for w in words:
        len_list.append(len(w))
    len_set = set(len_list)
    print(len_set)

    result = {}
    # 初始化每个长度为空列表
    for l in len_set:
        result[l] = []

    # 第二步：再次遍历单词，追加进去
    for w in words:
        l = len(w)
        result[l].append(w)
    return result


animals = ['apple', 'bat', 'cat', 'elephant', 'dog']
res = group_by_length(animals)
print(res)
# 输出 {5: ['apple'], 3: ['bat', 'cat', 'dog'], 8: ['elephant']}
