# 应用题
# ①
# 1. 英雄一代战机 (战斗力60) 和 敌军战机 (战斗力70) 对抗, 英雄1代战机失败
# 2. 卧薪尝胆, 英雄二代战机(战斗力80) 出场, 战斗成功
# 3. 对象对战平台 object_play 实现多次战斗

class MePlane1:
    def __init__(self, power=0):
        self.power = power

    def powers(self):
        return self.power


class MePlane2(MePlane1):
    def powers(self, power=2):
        return power


class YouPlane:
    def __init__(self, power):
        self.power = power

    def powers(self):
        return self.power


#   使用多态构建出来的函数
def object_play(me, you):
    if me.powers() > you.powers():
        print(
            f'多态: {me.__class__.__name__}(战斗力{me.powers()}) 赢了 {you.__class__.__name__}(战斗力{you.powers()})!')
    else:
        print(
            f'多态: {you.__class__.__name__}(战斗力{you.powers()}) 赢了 {me.__class__.__name__}(战斗力{me.powers()})!')


if __name__ == '__main__':
    # 1. 不用多态
    # 注意默认值
    # 第一架 / 第一次 战斗 结束
    # me = MePlane1().powers()
    # you = YouPlane().powers()
    # if me > you:
    #     print('第一次 我赢了')
    # else:
    #     print('第一次 你赢了')
    # # 第二架 / 第二次 战斗 结束
    #
    # me = MePlane2().powers()
    # you = YouPlane().powers()
    # if me > you:
    #     print('第二次 我赢了')
    # else:
    #     print('第二次 你赢了')
    #
    # 2. 使用多态
    object_play(MePlane1(60), YouPlane(70))

# 总结:
# 在不改变框架代码的情况下,
#   轻松实现模块和模块之间的解耦合 以及 软件系统的可拓展
# 解耦合解释:
#   减少模块或组件之间的直接依赖关系, 各部分能够独立存在和运行
# 可拓展解释:
#   指在不破坏现有功能的前提下，低成本添加新功能的能力

# 继承和多态对比:(打比方)
#   继承相当于:孩子可以复用老爹的东西。
#   多态相当于:老爹框架，不做任何修改的情况下
#       可以可拓展的使用后来人(孩子)写的东西
