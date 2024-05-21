from openai import OpenAI

from bot.openai_gpt.utils.const_value import API_key

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=API_key,
    base_url="https://api.chatanywhere.com.cn"
)

# 非流式响应
def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return completion.choices[0].message.content

def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    response = ""
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
    return response

def gpt_answer_questions(text):
    messages = [{'role': 'user','content': text}]
    # 非流式调用
    # gpt_35_api(messages)
    # 流式调用
    return gpt_35_api_stream(messages)
