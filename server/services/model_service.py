import json
import os
from pathlib import Path

class ModelService:
    def __init__(self, file_path='models.json'):
        self.file_path = Path(__file__).parent.parent / file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not self.file_path.exists():
            self.file_path.write_text(json.dumps({"models": []}))

    def load_models(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)['models']

    def add_model(self, new_model):
        data = json.loads(self.file_path.read_text())
        if new_model not in data['models']:
            data['models'].append(new_model)
            self.file_path.write_text(json.dumps(data, indent=4))
            return True
        return False