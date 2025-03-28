from openai import OpenAI
import httpx
import os

class LLMConfig:
    def __init__(self, api_key, base_url, model_name):
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name

class LLMService:
    MODEL_CONFIGS = {
        "free": LLMConfig(
            api_key=os.getenv("FREE_OPENAI_API_KEY"),
            base_url=os.getenv("FREE_OPENAI_BASE_URL"),
            model_name=os.getenv("FREE_OPENAI_MODEL_NAME")
        ),
        "deepseek": LLMConfig(
            api_key=os.getenv("DS_API_KEY"),
            base_url=os.getenv("DS_BASE_URL"),
            model_name=os.getenv("DS_MODEL_NAME")
        ),
        "gemini": LLMConfig(
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url=os.getenv("GEMINI_BASE_URL"),
            model_name=os.getenv("GEMINI_MODEL_NAME")
        ),
    }

    def __init__(self, model_type="free"):
        if model_type not in LLMService.MODEL_CONFIGS:
            raise ValueError(f"Unsupported model type: {model_type}")

        config = LLMService.MODEL_CONFIGS[model_type]
        self.client = OpenAI(api_key=config.api_key, base_url=config.base_url)
        self.model_name = config.model_name

    def _log_request(self, request):
        print(f"\n=== Request Details ===")
        print(f"URL: {request.url}")
        print(f"Method: {request.method}")
        print(f"Headers: { {k: '*****' if 'authorization' in k.lower() else v for k, v in request.headers.items()} }")
        print(f"Body Preview: {request.content[:200]}...")  # 截取前200字符

    def _log_response(self, response):
        print(f"\n=== Response Details ===")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Body Preview: {response.text[:500]}...")

    def get_completion(self, messages, stream=False):
        return self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            stream=stream
        )




