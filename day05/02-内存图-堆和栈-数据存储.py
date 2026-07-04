age = 20
print(id(age))  # 获取数据的存储地址

age1 = age

print(id(age1))

# 修改了 ↓ 地址了
age = 30
print(id(age))
# age ↑ 已被篡改

# ↓ 这个 还是原来的age 只不过 换 栈 了
print(id(age1))

# 2 6 11 行代码一样, 10 不一样

# 栈: 存储变量名  与 堆对象的映射关系 (引用), 不存储实际数据,快速但容量小
# 堆: 存储所有对象 (包括int,str,list等) 容量大但管理复杂
# 代码对象区: 存储编译后的字节码 (bytecode) 、函数名、常量、变量名等
