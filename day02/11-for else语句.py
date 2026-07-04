for i in range(1, 11):
    if i % 3 == 0:
        # break 结束至本文
        continue
else:
    print('语句正常结束,会执行到这里')
# 应用题
# ① 遍历遗传字符串,看是否有空格
str1 = 'asdasdsa dsaadas  dsfas'

for i in str1:
    if i == ' ':
        print('发现空格,循环已退出')
        break
else:
    print("这段没有空格")

#     总结:break非正常结束,continue属于正常结束
