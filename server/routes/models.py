from flask import Blueprint, request
from services.model_service import ModelService
from utils.response import StandardResponse, handle_errors

models_bp = Blueprint('models', __name__)
service = ModelService()

@models_bp.route('/models', methods=['GET'])
@handle_errors
def get_models():
    models = service.load_models()
    return StandardResponse(data={"models": models}).to_dict()

@models_bp.route('/models', methods=['POST'])
@handle_errors
def add_model():
    new_model = request.json.get('model')
    if not new_model:
        return StandardResponse(success=False, error="Missing model name").to_dict(), 400
    
    if service.add_model(new_model):
        return StandardResponse(data={"message": "Model added successfully"}).to_dict(), 201
    else:
        return StandardResponse(success=False, error="Model already exists").to_dict(), 400