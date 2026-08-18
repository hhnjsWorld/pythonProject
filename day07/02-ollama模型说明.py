# 总结思考:
# 1. ollama 作为
#   第三方的包 pip install 安装
#   本地工具 .exe / .dmg 安装

# 2. ollama -> 本地工具 -> 启动服务器 127.0.0.1:11434
#   -> 命令行 ollama run 'model' -> send message

# 3. apifox -> json请求 -> 借助 后端(看接口文档发送对应请求获取数据)
#   -> ollama工具(命令行 / 可视化chatbox)

# 4. streamlit框架 + ollama第三方包
#   ① pip install ...
#   ② streamlit -> 创建前端页面 -> streamlit run **.py
#       -> 启动服务 (localhost:8581) 打开网页
#       -> 提供组件 title / image / table 等标签

# 5. 输入框输入内容时 -> 发送 -> 本地模型交互
#       例如:
# ollama.chat(model='模型', messages=[{
# 'role': 'user', # 角色
# 'content': '聊天内容',
# }])

# 6. 下面学习目标
#       实现多轮对话
#       聊天存储器 -> 不是服务器
#       -> 对应的sql 配合 接口
#       -> 消息存储
