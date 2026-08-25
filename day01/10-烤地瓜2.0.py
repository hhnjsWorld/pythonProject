# ============================================
# 需求：烤地瓜 2.0
# ============================================
# 1. 地瓜被烤的时间是累加的：
#    0-3 分钟  → 生的
#    3-7 分钟  → 半生不熟
#    7-12 分钟 → 熟了
#    超过12分钟 → 已烤焦，糊了
#
# 2. 调料可以按食客意愿多次添加，每次添加都会记录下来
#
# 3. 打印地瓜对象时，能直接看到：烤了多少分钟、当前生熟程度、加了哪些调料
# ============================================


# 定义地瓜类
class SweetPotato:

    # __init__：初始化属性，创建地瓜时就有的初始数据
    def __init__(self):
        self.name = '地瓜'  # 名字
        self.time = 0  # 累计烤的时间（分钟），初始为0
        self.tiaoliao = []  # 调料列表，初始为空，后续可不断添加

    # __str__：打印对象时自动调用，返回地瓜当前的完整状态
    def __str__(self):
        # 根据累计时间判断生熟程度
        if self.time <= 0:
            degree = '生的'
        elif self.time <= 3:
            degree = '生的'
        elif self.time <= 7:
            degree = '半生不熟'
        elif self.time <= 12:
            degree = '熟了'
        else:
            degree = '已烤焦,糊了'
        # 把时间、生熟程度、调料信息一起返回
        return f'地瓜烤了{self.time}分钟，{degree}，添加的调料有!：{self.tiaoliao}'

    # cook：烤地瓜，每次传入本次烤的时间，累加到总时间上
    def cook(self, time):
        self.time += time  # 累加烤的时间（不是覆盖！）
        # 根据累加后的总时间，打印当前生熟状态
        if self.time <= 3:

            print(f'烤了{self.time}分钟，地瓜是生的')
        elif self.time <= 7:
            print(f'烤了{self.time}分钟，地瓜半生不熟')
        elif self.time <= 12:
            print(f'烤了{self.time}分钟，地瓜熟了')
        else:
            print(f'烤了{self.time}分钟，地瓜已烤焦，糊了')

    # add_tiaoliao：添加调料，把调料追加到列表中
    def add_tiaoliao(self, tiaoliao):
        # append 可用于添加
        # insert 统计展示前面每步的所添加的
        self.tiaoliao.insert(0, tiaoliao)  # insert(0, ...) 插到列表头部，最新的排最前
        # 用逗号拼接，打印当前所有调料
        print(f'添加了调料：{",".join(self.tiaoliao)}')


# ---- 测试代码 ----

# 1. 创建地瓜对象，此时 time=0，调料=[]
potato = SweetPotato()
print(potato)  # 输出：地瓜烤了0分钟，生的，添加的调料有：[]

# 2. 烤2分钟 → 累计2分钟 → 生的
potato.cook(2)  # 输出：烤了2分钟，地瓜是生的
# 加调料
potato.add_tiaoliao('辣椒粉')  # 输出：添加了调料：辣椒粉

# 3. 再烤3分钟 → 累计5分钟 → 半生不熟
potato.cook(3)  # 输出：烤了5分钟，地瓜半生不熟
# 再加调料
potato.add_tiaoliao('孜然')  # 输出：添加了调料：孜然

# 4. 再烤5分钟 → 累计10分钟 → 熟了
potato.cook(5)  # 输出：烤了10分钟，地瓜熟了
# 再加调料
potato.add_tiaoliao('蒜蓉')  # 输出：添加了调料：蒜蓉

# 5. 最终打印地瓜，查看完整状态
potatoAll = potato
print(potatoAll)  # 输出：地瓜烤了10分钟，熟了，添加的调料有：['辣椒粉', '孜然', '蒜蓉']
