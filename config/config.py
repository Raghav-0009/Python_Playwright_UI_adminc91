import json
import os

ENV = os.getenv("ENV", "qa")

def get_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "config", f"{ENV}.json")

    with open(config_path, "r") as file:
        return json.load(file)
