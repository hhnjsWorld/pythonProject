"""
需求: 学生对象 -> 字典
    __dict__ python内置的属性,作用: 将对象 转成字典

"""
from student import Student

if __name__ == '__main__':
    s = Student('老王', 18, '男', '1381381381381', '被包养了')
    # print(type(s)) # <class 'student.Student'>
    s_dict = s.__dict__  # dict
    # print(s_dict.age) # ❌
    print(s_dict)
    # print(type(s_dict))
    print('*' * 30)

    # 学生对象列表[Student(), xxxx] -> 字典列表[{},{}]
    students = [
        Student('老王1', 18, '男', '1381381381381', '被包养了'),
        Student('老王2', 18, '男', '1381381381381', '被包养了'),
        Student('老王3', 18, '男', '1381381381381', '被包养了'),
    ]

    # # 方法一
    # students_dict = []

    # for stu in students:
    #     students_dict.append(stu.__dict__)
    # print(students_dict)

    # 方法二
    # 列表推导式
    # __dict__: 对象列表转 字典列表
    students_dict = [stu.__dict__ for stu in students]
    print(students_dict)
    # 转回来
    students_obj = [Student(**stu) for stu in students_dict]


    def __str__(self):
        return f"学生姓名：{self.name},学生年龄：{self.age},学生性别：{self.sex},学生电话：{self.phone},学生描述：{self.desc}"


    for s in students_obj:
        print(s, '我是字符串')

    # 字典 -> 学生对象 (迎合现有的代码 -> 更改学生信息)
    # 更新学生的功能 -> 代码 -> 学生列表 ==> [学生对象1,学生对象2]
    # 修改 -> 学生对象.属性名 = 新值
    # 字典.属性名 = 值 # ❌ 不对

    # 举例
    my_dict = {
        'name': '小李',
        'age': 18,
        'sex': '男',
        'phone': '123456789',
        'desc': '美少男'
    }
    # ** 是 语法糖效果,值全拿
    res = Student(**my_dict)
    res1 = res.__dict__
    print(res1)
