from pydantic import BaseModel

class ChatRequest(BaseModel):
    """聊天请求数据结构模型"""
    messages: list  # 消息列表，包含角色和内容的对话消息
    stream: bool = False  # 是否使用流式响应，默认为否
