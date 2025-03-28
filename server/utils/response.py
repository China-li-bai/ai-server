from flask import jsonify
from dataclasses import dataclass

@dataclass
class StandardResponse:
    success: bool = True
    data: dict = None
    error: str = None

    def to_dict(self):
        return {
            "success": self.success,
            "data": self.data,
            "error": self.error
        }

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify(StandardResponse(success=False, error=str(e)).to_dict()), 500
    wrapper.__name__ = func.__name__
    return wrapper