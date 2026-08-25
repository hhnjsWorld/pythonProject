# 应用题:
# 单继承
#   摊煎饼的老师傅 Master, 摸爬滚打多年, 研发了一个精湛的煎饼技术
#   将这套技术传授给他最得意的徒弟 Prentice

# 自己写:
# 师父
# class Master(object):
#     def __init__(self):
#         self.skill = '摊煎饼'
#
#     def __str__(self):
#         return self.skill
#
#
# # 徒弟
# class Prentice(Master):
#
#     def __str__(self):
#         return self.skill
#
#
# MasterIs = Master()
# print(MasterIs)
#
# apprentice = Prentice()
# print(apprentice)

# 跟着做

# Master:Xufu
# apprentice: Save


class Xufu:
    def __init__(self):
        self.name = '徐福'
        self.skill = ' [古法徐福烩饭技术] '

    def make_cake(self):
        print(f'{self.name}运用{self.skill}制作烩饭')


class Save(Xufu):
    def __str__(self, who='赛夫'):
        return f'{self.name}的徒弟{who}也会{self.skill}'


# 实例函数
Master = Xufu()
Master.make_cake()
apprentice = Save()
print(apprentice)
