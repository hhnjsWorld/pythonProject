"""
该模块用来管理学生信息, 学生信息包含 年龄 / 性别 / 名字 / 手机号 / 描述

"""


class Student:
    """
        定义学生信息 (属性)
        :param name: 学生姓名
        :param age: 学生年龄
        :param sex: 学生性别
        :param phone: 学生电话
        :param desc: 学生描述
    """

    def __init__(self, name, age, sex, phone, desc):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone
        self.desc = desc

    def __str__(self):
        return (f'学生姓名: {self.name},学生年龄: {self.age},'
                f'学生性别: {self.sex},学生电话: {self.phone},学生描述: {self.desc}')


# 自测代码
if __name__ == '__main__':
    s = Student('老王', 18, '男', '1381381381381', '被包养了')
    print(s)
