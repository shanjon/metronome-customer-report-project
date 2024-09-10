import os

_config = None

def load_config():
    global _config
    _config = {
        "BASE_URL": "https://api.metronome.com/v1",
        "API_TOKEN": os.environ.get("METRONOME_API_TOKEN")
    }
    return _config

def get_config():
    global _config
    if _config is None:
        load_config()
    return _config