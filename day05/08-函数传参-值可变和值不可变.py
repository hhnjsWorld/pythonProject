def fn1(names):
    names.append(5)
    print('names', id(names))


name_list = [1, 2, 3, 4]
fn1(name_list)

print('name_list', id(name_list))


def fn2(num):
    num += 1
    print('num', num)  # 11


count = 10
fn2(count)
print('count', count) # 10

# 两个结果不一样,里面  num 为 11,外面 为 10
