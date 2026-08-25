"""
学生管理系统模块
学生添加 / 删除 / 修改 / 查询单个 / 查询多个
"""
from student import Student


class StudentCMS:
    """初始化学生的列表数据"""

    def __init__(self):
        # 学生的列表数据,默认为空
        self.stu_list = [
            Student('小白', 18, '女', '13813813813', '美女')
        ]  # 假数据,方便测试

    # 显示用户信息
    def show_view(self):
        print('\n', '*' * 30)
        print('学生管理系统pro')
        print('\t1. 添加学生')
        print('\t2. 删除学生')
        print('\t3. 修改学生')
        print('\t4. 查询学生')
        print('\t5. 显示所有学生')
        print('\t6. 保存学生信息')
        print('\t0. 退出系统')
        print('*' * 30, '\n')

    # 添加学生信息
    def add_stu(self):
        # 添加 并 不可重名
        name = input('请输入学生姓名: ')
        for stu in self.stu_list:
            if stu.name == name:
                print('添加学生信息失败,学生已存在')
                break
        else:
            self.stu_list.append(
                Student(name, input('请输入学生年龄: '), input('请输入学生性别: '), input('请输入学生电话: '),
                        input('请输入学生描述: ')))
            print('添加学生信息成功')

    # 删除学生信息
    def delete_stu(self):
        # 一行代码删除
        name = input('请输入学生姓名: ')
        self.stu_list = [stu for stu in self.stu_list if stu.name != name]
        print('删除学生信息成功')

    # 修改学生信息
    def update_stu(self):

        name = input('请输入学生姓名: ')
        for stu in self.stu_list:
            if stu.name == name:
                stu.name = input('请输入学生姓名: ')
                stu.age = input('请输入学生年龄: ')
                stu.sex = input('请输入学生性别: ')
                stu.phone = input('请输入学生电话: ')
                stu.desc = input('请输入学生描述: ')
                print('修改学生信息成功')
                break
        else:
            print('修改学生信息失败,没有找到该学生')

    # 查询单个学生信息
    def query_stu(self):
        name = input('请输入学生姓名: ')
        for stu in self.stu_list:
            if stu.name == name:
                print(stu)
                break
        else:
            print('查询学生信息失败,没有找到该学生')

    # 显示全部学生信息
    def query_all_stu(self):
        # 显示所有学生信息
        if len(self.stu_list) > 0:
            for stu in self.stu_list:
                print(stu)
        else:
            print('没有学生信息')

    # 保存学生信息
    def save_stu(self):
        pass

    def start(self):
        while True:
            # 显示操作页面
            self.show_view()
            # 获取用户输入
            input_num = input('请输入功能数字编号: ')
            if input_num == '1':
                print('添加学生信息')
                self.add_stu()
            elif input_num == '2':
                print('删除学生信息')
                self.delete_stu()
            elif input_num == '3':
                print('修改学生信息')
                self.update_stu()
            elif input_num == '4':
                print('查询学生信息')
                self.query_stu()
            elif input_num == '5':
                print('显示所有学生信息')
                self.query_all_stu()
            elif input_num == '6':
                print('保存学生信息')
                self.save_stu()
            elif input_num == '0':
                exit_res = input('确定要退出系统吗? y/n: ')
                # y or Y 表示退出系统
                if exit_res.lower() == 'y':
                    print('退出系统')
                    break
                else:
                    print('继续运行系统')
            else:
                print('输入有误,请重新输入')


if __name__ == '__main__':
    # 创建学生系统
    cms = StudentCMS()
    cms.start()
