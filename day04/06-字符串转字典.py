s = "name=坤坤;age=18;desc=唱跳rap篮球"
item_list = s.split(";")
print(item_list)

item_list = ['name=坤坤', 'age=18', 'desc=唱跳rap篮球']
for item in item_list:
    k, v = item.split("=")
    print(v)

s = "name=坤坤;age=18;desc=唱跳rap篮球"
item_list = s.split(";")
my_dict = {}
for item in item_list:
    name = item[0:item.index("=", 0):]
    value = item[item.index("=", 0) + 1::]
    print(value)
    # name, value = item.split("=")
    if name == "desc":
        my_dict["hobby"] = value
    else:
        my_dict[name] = value
    print(my_dict)

    data_str = "username=小明;gender=男;score=90"
    item_list = data_str.split(";")
    d = {}
    for item in item_list:
        k, v = item.split("=")
    if k == "score":
        d[k] = int(v)
    else:
        d[k] = v
    print(d)

    data_str = "username=小明;gender=男;score=90"
    item_list = data_str.split(";")
    res = {k: int(v) if k == "score" else v for k, v in [x.split("=") for x in item_list]}
    print(res)
