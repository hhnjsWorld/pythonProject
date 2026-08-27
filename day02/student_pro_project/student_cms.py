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
            # Student('小白', 18, '女', '13813813813', '美女')
        ]  # 假数据,方便测试

    # 显示用户信息 展示
    @staticmethod # 静态方法
    def show_view():
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

    # 添加学生信息 增
    def add_stu(self):
        # 添加 并 不可重名
        name = input('请输入学生姓名: ')
        # 循环遍历
        for stu in self.stu_list:
            if stu.name == name:
                print('添加学生信息失败,学生已存在!')
                break
        # TODO: for 循环后面接 else 表示 for 循环正常结束 / 退出,(非 break强制退出) -> 都会执行 else
        else:
            self.stu_list.append(
                Student(name, input('请输入学生年龄: '), input('请输入学生性别: '), input('请输入学生电话: '),
                        input('请输入学生描述: ')))
            print('添加学生成功')

    # 删除学生信息 删
    def delete_stu(self):
        # 一行代码删除 要做判断
        name = input('请输入学生姓名: ')
        for stu in self.stu_list:
            if stu.name == name:
                # remove
                self.stu_list.remove(stu)
                # 这是一个列表推导式，作用是从列表中过滤掉指定姓名的学生，等价于删除操作。 remove 也行
                # self.stu_list = [stu for stu in self.stu_list if stu.name != name]
                # print('删除学生信息成功')
                # break
                print('删除学生信息成功')
                break
        else:
            print('删除学生信息失败,没有找到该学生')

    # 修改学生信息 改
    def update_stu(self):

        # 一行代码解决 要做判断
        name = input('请输入学生姓名: ')
        for stu in self.stu_list:
            if stu.name == name:
                # 这是一个列表推导式，作用是从列表中过滤掉指定姓名的学生，等价于删除操作。
                self.stu_list = [stu for stu in self.stu_list if stu.name != name]
                self.stu_list.append(
                    Student(name, input('请输入学生年龄: '), input('请输入学生性别: '), input('请输入学生电话: '),
                            input('请输入学生描述: ')))
                print('修改学生信息成功')
                break

        else:
            print('修改学生信息失败,没有找到该学生!!!')

    # 查询单个学生信息 查单
    def query_stu(self):
        name = input('请输入学生姓名: ')
        for stu in self.stu_list:
            if stu.name == name:
                print(stu)
                break
        else:
            print('查询学生信息失败,没有找到该学生')

    # 显示全部学生信息 查全
    def query_all_stu(self):
        # 显示所有学生信息
        if len(self.stu_list) > 0:
            for stu in self.stu_list:
                print(stu)
        else:
            print('没有学生信息')

    # 保存学生信息 保存
    # 下面为啥这么做?
    #   存学生信息 -> 写入文件 -> 学生对象 -> 字典格式
    #   取学生信息 -> 读取文件 -> 字典格式 -> 学生对象
    def save_stu(self):
        # with可以开启上下文进行管理的写法 / 也可close()
        # 1.打开文件 - 写 - 指定编码格式 utf-8 -> f
        with open('student.txt', 'w', encoding='utf-8') as f:
            # 转成字典列表
            stu_dict_list = [stu.__dict__ for stu in self.stu_list]
            # 写入
            f.write(str(stu_dict_list))  # 为什么str? 因为文件中只能写字符串
        # 问题: 存储的是学生对象的地址信息, 影响后期操作 -> TODO -> 学生对象 -> 字典

    # 读取学生信息 -> 列表推导式 -> 学生对象
    def load_student(self):
        # 1. 加入异常处理, 有可能文件不存在.
        try:
            # 2. 关联学生信息文件.
            with open('./student.txt', 'r', encoding='utf-8') as src_f:
                # 3. 一次性读取所有数据.
                stu_data = src_f.read()  # '[字典, 字典...]'
                # 4. 把上述的字符串, 转为列表.
                stu_list = eval(stu_data)  # ''
                # 5. 判断如果列表为空, 就赋予空列表.
                if len(stu_list) == 0:
                    stu_list = []
                # 6. 把stu_list(列表套字典) 转成 [学生对象, 学生对象...], 并赋值给 self.stu_list
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            # 7. 走这里, 说明目的地文件不存在, 创建即可.
            with open('./student.txt', 'w', encoding='utf-8') as src_f:
                pass

    def start(self):
        # 加载学生信息
        self.load_student()
        while True:
            # 显示操作页面
            # 可以使用类名调用静态方法
            StudentCMS.show_view()  # 使用类名调用静态方法
            # 或者使用self调用静态方法
            # self.show_view()

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
                print('保存学生信息成功')

            elif input_num == '0':
                exit_res = input('确定要退出系统吗? y/n: ')
                # y or Y 表示退出系统
                if exit_res.lower() == 'y':
                    # 主动保存学生信息 -> 防止用户退出时, 数据丢失
                    self.save_stu()

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
