# 位置参数
# 1. 必须按照位置传递 def desc(a,b)  (猫,狗)
# 2. 形参实参的个数也要保持一致
# 形式一
def animal_fn(animal_type, animal_name):
    """
    宠物相关
    参数1: animal_type,
    参数2: animal_name
    :return:
    """
    print(f'我有一只宠物,品种是{animal_type},名字叫{animal_name}')


animal_fn('拉布拉多', '黑皮')


# animal_fn('黑皮', '拉布拉多') #❌

# 形式二
def animal_fn(animal_type, animal_name):
    """
    宠物相关
    参数1: animal_type,
    参数2: animal_name
    :return:
    """
    print(f'我有一只宠物,品种是{animal_type},名字叫{animal_name}')


# 如果 参数倒置 , 写上关键字参数 不会 改变前后
animal_fn(animal_name='黑皮', animal_type='拉布拉多')

# 位置参数可以和关键字参数 一起使用
# 要求: 位置参数必须在前 , 关键字参数可在后

# 错误示范
# animal_fn(animal_type='哈士奇', '大傻') # ❌
# animal_fn(animal_name='土狗', '大聪明') # ❌

# 形式三
def desc(person, skill='烹饪'):
    """
    :param person: 人物
    :param skill:  技能
    :return: 我是**,我会**
    """
    return f'我是{person},我会{skill}'


result = desc(person='李大嘴', skill='地锅鸡')
print(result)

result1 = desc('王大厨')
print(result1)  # 参数置前

result11 = desc(person='王大厨')
print(result11)  # 参数置前

result2 = desc('王大厨', '一锅鲜')
print(result2)


