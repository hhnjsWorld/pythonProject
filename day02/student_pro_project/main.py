"""
程序的入口文件

"""
from student_cms import StudentCMS

if __name__ == '__main__':
    # 创建学生管理系统对象
    cms = StudentCMS()
    # 启动系统
    cms.start()
