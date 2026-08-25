# 举例:
# class Student: 独立的类
# class Student(): ...

# class Student( Person ): 学生类继承自Person类
#   -> Person类身上的属性和行为拿来为己使用
# class Person( object )
#   -> 人类 类

#   ↑ 理解为:student 继承自->  person 继承自-> object 的关系
#       所以说 python 中  一切皆对象

"""

python中继承: 讲别的类中的属性和方法 拿来用
    一切类 直接或者间接继承自object 一切皆对象 object就是最顶层对象

"""


class Father(object):
    def __init__(self):
        self.gender = '男'

    def walk(self, who='爸爸'):
        print(f'{who}会散步,锻炼身体')


# 1. 基础概念
#   打比方: 1个儿子
# class Son(Father):
#     pass
#
#
# s = Son()
# print(f'性别: {s.gender}')
# s.walk()

#   打比方: 2个儿子


# 大儿子 会游泳
class Son1(Father):
    def swimming(self, who='大儿子'):
        print(f'{who}{self.gender}游泳')


s1 = Son1()
s1.swimming()


# 小儿子 会吹牛
class Son2(Father):
    def chuiniu(self, who='小儿子'):
        print(f'{who}{self.gender}吹牛')


s2 = Son2()
s2.chuiniu()

far = Father()
far.walk()
