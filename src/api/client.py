import requests
from src.utils.config import get_config

class MetronomeClient:
    def __init__(self):
        config = get_config()
        self.base_url = config["BASE_URL"]
        self.headers = {
            "Authorization": f"Bearer {config['API_TOKEN']}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, payload):
        response = requests.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()