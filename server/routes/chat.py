from flask import Blueprint, request, jsonify, Response
from services.llm_service import LLMService
import logging

# Define the blueprint
chat_bp = Blueprint('chat', __name__)
# Configure logging
# logger = logging.getLogger(__name__)

# Define the route
@chat_bp.route('/chat/completions', methods=['POST'])
def chat_completions():
    """
    API 端点示例
    Request Body:
    {
        "messages": [
            {"role": "system", "content": "你是一个助手"},
            {"role": "user", "content": "你好"}
        ],
        "stream": false
    }
    """
    data = request.get_json()
    messages = data.get('messages', [])
    stream = data.get('stream', False)
    llm_client = LLMService(model_type="free")

    if stream:
        def generate():
            stream = llm_client.get_completion(messages, stream=True)
            for chunk in stream:
                if chunk.choices:
                    yield chunk.choices[0].delta.content or ""

        return Response(generate(), mimetype='text/event-stream')
    else:
        completion = llm_client.get_completion(messages, stream=False)
        return jsonify({
            "content": completion.choices[0].message.content
        })