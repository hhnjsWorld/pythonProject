# 1. 设定账号和密码
username = 'admin'
password = '123456'
for i in range(0, 3):  # -> i 0 1 2
    # 2. 获取用户输入的用户名和密码
    uname = input('请输入用户名: ')
    pwd = input("请输入密码: ")
    if (uname == username) and (password == pwd):
        print(f'欢迎光临!{uname}')
        break
    else:
        count = 2
        # 嵌套
        if i < 2:
            print(f"输入错误,还有{count - i}次机会")
        else:
            print('密码错误,系统已锁定')

    #
    #
    # # 应用题
    # # ① 登陆系统 只有三次机会
    # def set_system():
    #     # 设置密码
    #     while True:
    #         password = input("请输入初始密码：")
    #
    #         if password.startswith("-"):
    #             print("❌ 密码不能是负数")
    #             continue
    #
    #         if not password.isdigit():
    #             print("❌ 请输入数字")
    #             continue
    #
    #         if len(password) != 6:
    #             print("❌ 密码必须是6位数字")
    #             continue
    #
    #         print("✅ 密码设置成功")
    #         break
    #
    #     # 登录3次机会
    #     count = 3
    #
    #     while count > 0:
    #
    #         passwordInto = input("请输入密码登录：")
    #
    #         if passwordInto == password:
    #             print("✅ 密码登录成功")
    #             return True
    #
    #         else:
    #             count -= 1
    #             print(f"❌ 密码错误，剩余{count}次机会")
    #
    #     print("🚫 三次机会用完，系统锁定")
    #     return False
    #
    #
    # passIs = set_system()
    #
    # print(passIs)
