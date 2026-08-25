# ============================================
# 应用题:通信方式 - 继承
# ============================================
# 父类:Communication（通信方式）
#   - 发送消息 send_message
#   - 接受消息 receive_message
#
# 子类:Letter（写信），继承自 Communication
#   - 重写 - 发送消息 send_message:
#       1. 准备信纸信封
#       2. 手写或打印内容
#       3. 贴邮票投递邮箱
#   - 重写 - 接受消息 receive_message:
#       1. 检查邮箱
#       2. 拆开信封
#       3. 阅读信纸内容
#   - 扩展属于子类自己的属性和方法
# ============================================

# 通讯方式
class Communication:

    def message(self):
        self.sender = '刘德华'
        self.receiver = '梁朝伟'
        self.content = '其实我不是卧底'

        return f'{self.sender}发信息,{self.receiver}接受,信的内容为{self.content}'


class Kill:
    def kill(self):
        self.sender = '刘德华'
        self.receiver = '梁朝伟'
        self.content = '其实我不是卧底'

        return f'{self.sender}拿着枪对着{self.receiver},说了{self.content}'


class Letter(Communication, Kill):
    def __init__(self):
        self.gang = 'AK47已经准备好'

    def __str__(self):
        return self.gang


# def view(self):
#     print('查阅信件')


print(Letter(), Letter().kill())
