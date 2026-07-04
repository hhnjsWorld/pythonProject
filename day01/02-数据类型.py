# 数据类型
# 一、基础:数值 布尔值 字符串str
#    进阶:list列表 tuple元组 set集合 dict字典
# 快捷键 shift + alt + 鼠标选中
name = '吴亦凡'
age = 44
sexy = '男'
height = 1.78
print(type(name))
print(type(age))
print(type(sexy))
print(type(height))

stu_name = '蔡徐坤'
print(stu_name)
stu_age = 16
print(stu_age)
stu_height = 1.656
print(stu_height)
stu_id = 25
print(stu_id)
# 拼接
print('姓名 %s ' % stu_name)
print('姓名 %s 年龄 %d 身高 %f ' % (stu_name, stu_age, stu_height))

# %03d 3d意思空格占位,  03d = 年龄 016, 05d = 年龄 00016
print('年龄 %03d ' % stu_age)
# %.2f 2f意思小数点取后几位,可四舍五入,超长位补0
print('身高 %.2f' % stu_height)

# format格式
print('学生姓名 {} , 学生年龄 {}'.format(stu_name, stu_age))
# 格式简化
print(f'学生的姓名: {stu_name} -- 学生的年龄: {stu_age:010d} -- 学生的身高: {stu_height:.3f} -- 学生的id: {stu_id:03d}')

# \n 换行 \t 空格
print('hello\nhhn')
print('hello\nhhn')



