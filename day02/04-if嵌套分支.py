#  应用题
# ① 喝酒(嵌套写法)

def get_drunk_driving(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ 当前数字不能是负数")
                continue
            if value >= 20 / 100:
                if value < 80 / 100:
                    drunk = '酒驾了'
                else:
                    drunk = '醉驾了'
            elif 0 < value < 20 / 100:
                drunk = '合格驾驶'
            else:
                drunk = '没喝'

            return drunk

        except ValueError:
            print('❌ 请输酒精含量')
            continue


alcohol = get_drunk_driving('请输入酒精含量：')
print('当前酒精度是：', alcohol)


# ② 游戏设计练习(嵌套)

def get_role_skill(role, mana):
    while True:
        try:
            roles = input(role)
            roles_is = ['法师', '战士']
            if roles not in roles_is:
                print('❌ 请输入法师或者战士')
                continue
            value = float(input(mana))
            if value < 0:
                print("❌ 当前法力值已小于0")
                continue
            if roles == '法师':

                if value >= 50:
                    if value >= 100:
                        systemInfo = '大火球术'
                    else:
                        systemInfo = '冰冻雨'
                else:
                    systemInfo = "闪电雨"
            else:

                if value >= 50:
                    if value >= 100:
                        systemInfo = '致命一拳'
                    else:
                        systemInfo = '两拳'
                else:
                    systemInfo = "一拳"
            return ('我用' + roles + '角色施放了' + systemInfo + '技能')



        except ValueError:
            print('❌ 请输入角色')
            continue


roleMana = get_role_skill('请输入角色：', '请输入法力值：')

print(roleMana)
