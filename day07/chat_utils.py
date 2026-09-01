# 聊天机器人案例-封装chat_utils模块
"""

该模块充当 聊天机器人 的 后端模块 -> 接受前端Streamlit传来的用户问题
将问题 交给 大芸雁模型 deepseek,qwen 获取模型返回的结果 -> 返回给前端

"""
# 需求
# ① 构建一个基于大模型的本地智能聊天机器人
# ② 请求模块 - 向服务器请求数据
#       调用模型 -> 获取结果
#       chat_utils模块
#           1. 接受前端Streamlist传过来的用户问题
#           2. 交给大预言模型,获取结果,并返回
#           步骤
#               1. 导包
#   `           2. 定义函数请求拿结果
#               3. 测试函数

# ③ 前端模块 - 收集用户输入 , 调用请求模块
import ollama


def get_response(prompt):
    # 显式指定 host，避免 localhost 解析到 IPv6
    client = ollama.Client(host='http://127.0.0.1:11434')
    response = client.chat(
        model='deepseek-r1:1.5b',

        # messages=[{'role': 'user', 'content': prompt}]
        # [{'role': 'user', 'content': prompt}] 换成 prompt 有我们说的话 Ai说的话 是一个消息列表
        messages=prompt
    )
    return response.message.content


if __name__ == '__main__':
    prompt = input('请输入问题: ')
    res = get_response(prompt)
    print(res)
