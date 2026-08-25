# 应用题
# ①
# 1. 英雄一代战机 (战斗力60) 和 敌军战机 (战斗力70) 对抗, 英雄1代战机失败
# 2. 卧薪尝胆, 英雄二代战机(战斗力80) 出场, 战斗成功
# 3. 对象对战平台 object_play 实现多次战斗


class Plane:
    def __init__(self, power):
        self.plane = '战斗机'
        self.power = power

    def fight(self):
        pass


class PlaneMe(Plane):
    def __init__(self, power):
        super().__init__(power)

    def fight(self):
        print(f'英雄战机(战斗力{self.power})出击！')


class PlaneYou(Plane):
    def __init__(self, power):
        super().__init__(power)

    def fight(self):
        print(f'敌军战机(战斗力{self.power})出击！')


def object_play(plane1, plane2):
    plane1.fight()
    plane2.fight()
    if plane1.power > plane2.power:
        print(f'{plane1.plane} {plane1.__class__.__name__} 胜利！\n')
    else:
        print(f'{plane2.plane} {plane2.__class__.__name__} 胜利！\n')


PlaneMe1 = PlaneMe(60)
PlaneMe2 = PlaneMe(80)
PlaneYou = PlaneYou(70)


object_play(PlaneMe1, PlaneYou)
object_play(PlaneMe2, PlaneYou)
