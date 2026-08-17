# python 与 模型 交互
# 需求
# ① 导包
# 如果 我连vpn 就写下面这个
# import os
# os.environ['NO_PROXY'] = 'localhost,127.0.0.1'
import ollama

# 做多轮判断
while True:
    prompt = input('请输入您的问题: ')
    # 判我指令 'bb' 会终止
    if prompt == 'bb':
        break

    # ② 调用 ollama.chat(model='xx',message=[{},{}]) 函数
    result = ollama.chat(model='deepseek-r1:7b', messages=[{
        'role': 'user',
        'content': prompt,
    }])
    # ③ 从相应信息中,提取模型的回复结果,并且打印
    #   1. 第一种取出结果的方法
    print(f"机器人返回的结果: {result['message']['content']}")

    #   2. 第二种取结果的方法
    print(f"机器人返回的结果: {result.message.content}")
