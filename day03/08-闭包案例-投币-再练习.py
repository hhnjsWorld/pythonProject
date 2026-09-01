# 外层函数 Game,内部变量 coin 投币数量
# 内层函数 add , 对投币数量进行添加
#  内部函数 play, 对投币数量进行减少
#  返回 [ add,play ] 调用测试
def Game(coin=100):
    coin1 = coin
    def add(coin):
        nonlocal coin1
        coin1 += coin
        print(f'当前金币: {coin1}')

    def play(coin):
        nonlocal coin1
        coin1 -= coin
        print(f'当前金币: {coin1}')
    return add, play  # (add,play)


# 巧妙利用拆包的用法
add, play = Game(5000)

add(10)
add(20)
add(30)
add(40)
add(50)
play(10)
play(20)
play(30)
play(40)
play(50)
