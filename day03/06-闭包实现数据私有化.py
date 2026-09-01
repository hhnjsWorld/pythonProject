# 应用题
# ①
# 1. 定义一个外部函数 outer, 声明局部变量 count = 0
# 2. 内部声明一个函数 inner, 在 inner 中 让 count += 1
# 3. 返回 inner 函数

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(f'+=后的值: {count}')

    return inner


# 这样不会 调用 += 失效
# 三次 outer ()() 创建了三个独立的 count，互不相干
outer()()
outer()()
outer()()

# 应该这样
# 只调用了一次 outer ()，所以只有一个 count，后续多次 res () 都操作同一个 count，自然就累积了。
res = outer()  # inner -> count 已经被 res 引用了
# 变化的过程,除非手动释放,不然缓存一直都在
res()  # 0 -> 1
res()  # 1 -> 2
res()  # 2 -> 3
# python 具备垃圾回收机制,
#   变量 -> 没有被引用 -> 自动回收

# 闭包可以实现数据私有化,因为内部函数 有对 外部 变量的引用

# Todo:拓展知识:
#   res = outer()   # 闭包创建，count 被锁住
#   res()           # 0 → 1
#   res()           # 1 → 2
#   res()           # 2 → 3
#   手动释放
#   del res         # 解除对 inner 函数的引用
#                   # → inner 的引用计数归零
#                   # → __closure__ 被销毁
#                   # → cell 对象引用计数归零
#                   # → count 被回收
#   res.__closure__[0].cell_contents = None   # 把大对象替换为 None，释放内存
#   闭包通过 `__closure__` → cell → 变量 的引用链，让外层局部变量逃过引用计数的回收；这本身是设计特性，不是 bug。
#   只有当闭包长期持有大对象、形成带 `__del__` 的循环引用、或闭包集合无限增长时，才构成真正的内存泄漏。
#   释放方式就是 `del` 掉持有闭包的变量，让引用计数归零。