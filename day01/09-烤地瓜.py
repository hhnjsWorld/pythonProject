# 需求
# 地瓜被烤的时间
#   0-3 分钟 = 生的
#   3-7 分钟 = 半生不熟
#   7-12 分钟 = 熟了
#   超过 12 分钟 = 已烤焦, 糊了

#   添加的调料 = 食客可以按自己的愿意添加调料

class Vegetable:

    def __init__(self, name='地瓜', time=1, tiaoliao=None):
        self.name = name
        self.time = time
        # 避免可变默认参数陷阱：None 时再创建新列表
        self.tiaoliao = tiaoliao if tiaoliao is not None else []

    def __str__(self):
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
        return f'烤{self.name}咯,烤了{self.time}分钟,{degree},要放调料{self.tiaoliao}'

    def make_fn(self, time, tiaoliao):
        if time <= 0:
            return f'❌ 你没有时间去烤{self.name}'

        # 累加时间
        self.time += time

        # 判断生熟程度
        if self.time <= 3:
            degree = '生的'
        elif self.time <= 7:
            degree = '半生不熟'
        elif self.time <= 12:
            degree = '熟了'
        else:
            degree = '已烤焦,糊了'

        # 新调料插到列表头部，保留所有历史调料
        self.tiaoliao.insert(0, tiaoliao)

        return f'{self.name}烤了{self.time}分钟,{degree},放了{",".join(self.tiaoliao)}'


sweet_potato = Vegetable()
# print(sweet_potato)

sweet_potato_make = sweet_potato.make_fn(0, '辣椒粉')
print(sweet_potato_make)

# sweet_potato_make = sweet_potato.make_fn(3, '孜然')
# print(sweet_potato_make)
#
# sweet_potato_make = sweet_potato.make_fn(5, '蒜蓉')
# print(sweet_potato_make)

print(sweet_potato)
