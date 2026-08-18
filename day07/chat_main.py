# ###
# 该模块充当聊天机器人的前后端 → 接收用户输入的问题，
# 调用 chat_utils 模块中的 get_response() 函数 获取模型结果
# 最终：通过streamlit 在前端显示

###

# 1. 导包
# ① 搭建聊天界面
import streamlit as st

# ② langchain 库：聊天机器人核心的模块
# ConversationBufferMemory：聊天记录存储区
from langchain_classic.memory import ConversationBufferMemory

# ③ 自定义模块 chat_utils 获取模型的结果
from chat_utils import get_response

# 2. 页面标题
st.title("聊天")

# 3. 判断是否有历史消息记录对象，如果没有的就创建，存储所有的消息记录
# st.session_state 存储会话状态数据的字典（存储会话数据）
if 'memory' not in st.session_state:
    # 3.1 创建一个对象 ConversationBufferMemory -> 存储到session_state状态中
    # ConversationBufferMemory 专门存储和管理多轮对话历史
    st.session_state.memory = ConversationBufferMemory()

    # 3.2 添加机器人欢迎语 初始对话先装 -> 容器 st.session_state.messages
    st.session_state.messages = [{"role": "assistant", "content": "你好，我是你的AI助手，有什么可以帮助到你的么？"}]

# 4. 遍历 session_state的messages 消息列表 - 显示到页面上
for message in st.session_state.messages:
    # 4.1 streamlit 提供了 with语句，通过聊天消息容器，用来显示当前角色（user / assistant）的内容
    with st.chat_message(message['role']):
        # 该角色的消息容器内容显示 markdown / write
        st.markdown(message['content'])

# 5. 获取用户输入的内容
prompt = st.chat_input("请输入你的问题...")

# 6. 判断用户是否输入了内容
if prompt:
    # 6.1 把用户输入的消息 添加到 messages 列表中 / 将消息添加到历史记录中 (和渲染没关系) ->
    #   Todo: 发送给服务器 -> 数据库存储
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 6.2 在页面上显示 用户 输入的消息 / 指定渲染 (markdown(消息))
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner('Ai正在思考中...'):
        # 思考的时间 -> 原因模型返回数据消耗的时间
        # st.session_state.messages[{ "我们说的话,内容..." },{ ai回复的... }] 完整的对话历史记录传过去
        # 而不是 自己说的内容 (否则他是无法推测能力 / 上下文能力...)
        response = get_response(st.session_state.messages)

    # 6.3 将模型返回的结果 添加到历史记录中, 渲染到页面上
    st.session_state.messages.append({
        'role': 'assistant', 'content': response
    })
    # 6.4 把 response 渲染出来
    st.chat_message('assistant').markdown(response)
