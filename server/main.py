# ... existing imports ...
from routes import chat_bp, models_bp  # Ensure correct import
from services import LLMService, ModelService
from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Register blueprints
app.register_blueprint(chat_bp, url_prefix='/v1')
app.register_blueprint(models_bp, url_prefix='/v1')

# 移除原来的 chat_completions 路由定义
# 添加路由列表打印（调试用）
print("Registered routes:")
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200, debug=os.getenv("FLASK_DEBUG", False))