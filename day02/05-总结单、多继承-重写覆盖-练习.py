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


# 父类：通信方式
class Communication:

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        # 被 继承者 调起 通讯
        print(f'【父类初始化】创建通信对象：{self.sender} → {self.receiver}')

    def send_message(self):
        print(f'[{self.sender}] 发送消息给 [{self.receiver}]：通用发送方式')

    def receive_message(self):
        print(f'[{self.receiver}] 接受消息：通用接收方式')

    def show_status(self):
        print(f'通信状态：{self.sender} 与 {self.receiver} 正在通信中')


# 子类：写信，继承自 Communication
class Letter(Communication):

    # 扩展：子类自己的属性
    def __init__(self, sender, receiver, content='', stamp='普通邮票'):
        super().__init__(sender, receiver)  # 【父类初始化】创建通信对象：
        self.content = content
        self.stamp = stamp
        print(f'【子类初始化】信件内容：{self.content}，邮票：{self.stamp}\n')

    # 重写：发送消息（写信的流程）
    def send_message(self):
        print(f'--- {self.sender} 寄信给 {self.receiver} ---')
        # return
        print('1. 准备信纸信封')
        print(f'2. 手写内容：{self.content}')
        print(f'3. 贴{self.stamp}，投递邮箱')
        print('信件已寄出！\n')

    # 重写：接受消息（收信的流程）
    def receive_message(self):
        print(f'--- {self.receiver} 收信 ---')
        print('1. 检查邮箱')
        print('2. 拆开信封')
        print(f'3. 阅读内容：{self.content}')
        print('信件已读完！\n')

    # 扩展：子类自己的方法
    def show_info(self):
        print(f'寄信人：{self.sender}，收信人：{self.receiver}，内容：{self.content}')


# ---- 测试 ----

print('===== 1. 父类对象 =====')
comm = Communication('小9', '小红')
comm.send_message()
comm.receive_message()
comm.show_status()

print('\n===== 2. 子类对象（重写的方法）=====')
letter = Letter('老八迷之小憨包', '小红', '你好，最近怎么样？', '纪念邮票')
letter.send_message()  # 调用子类重写的方法
letter.receive_message()  # 调用子类重写的方法

print('===== 3. 子类对象（继承父类的方法）=====')
letter.show_status()  # 直接继承父类方法，子类没有重写

print('\n===== 4. 子类对象（扩展的方法）=====')
letter.show_info()  # 子类自己扩展的方法
