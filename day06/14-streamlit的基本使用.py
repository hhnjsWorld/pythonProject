import streamlit as st

st.title('我是机器人')

# 标题
st.write('这是一个段落的标签')
st.write('这是一个段落的标签')
st.write('这是一个段落的标签')

# 多级标题
st.write('# 一级标题')
st.write('## 二级标题')
st.write('### 三级标题')

# 写入图片
st.image('./data/hand.png', width=100)

# 分割线
st.divider()

# st.table({字典}) # 字典格式如下
st.table(data={'name': ['张三'], 'age': [20], 'city': ['北京']})

# 写入输入框
name = st.text_input('请输入你的名字: ')
if name:
    st.write(f'欢迎{name}')

# 密码输入框
st.text_input('密码是多少? : ', type='password')

# 数字输入框 最小 和 最大 的年龄限制
st.number_input('年龄: ', step=1, min_value=10, value=20, max_value=30)

# 多行文本
st.text_area('请输入多行内容: ')

# 消息容器
prompt = st.chat_input('请输入问题: ')
if prompt:
    st.write(f'用户输入的问题: {prompt}')
