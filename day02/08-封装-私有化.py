# 没有私有权限的情况
#   把属性和方法,写到类里面的 就是封装
#   可以为属性和方法添加私有权限

# 又私有权限的情况 (保护我们的数据、方法)
#   账户余额只能通过暴露的方法改

# 在属性或者方法前面加上__
# 私有属性
#   __属性名

# 私有方法
#   def __方法名():

"""
封装: 将数据 和 方法 放到类 中

私有属性和方法 - 针对于隐私的数据或者函数进行不对外暴露的体现
__属性名
__方法名
智能在类的内部访问 , 外部是访问不了的

"""


# 应用题
# ① 银行存取钱
class BankAccount:
    def __init__(self):
        self.bank_name = '中国工商银行'
        self.bank_balance = 10000
        # self._name = '李小龙'
        self.__nameEncrypt = '李小龙'  # 属于私有的属性

    def save_money(self, money):
        self.bank_balance += money

    def with_draw(self, money):
        self.bank_balance -= money

    def __show_money(self):
        print(f'{self.bank_name}余额为: {self.bank_balance},用户{self.__nameEncrypt}存的')


# 用户 在银行相关的信息 -> 暴露在外 / 不安全
bank = BankAccount()
bank.save_money(1000)
bank.with_draw(1000)
bank.with_draw(1000)

print(bank.bank_name)
print(bank.bank_balance)

print(bank.__nameEncrypt)  # 属于私有的属性,无法在类外部访问类内部的私有属性
# bank.show_money() # 可以看到用户
bank.__show_money() # 已看不到
