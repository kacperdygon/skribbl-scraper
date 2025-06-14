"""Global things"""
import json
import os
from colorama import Fore, Style

def load_config():
    """Returns config from config.json"""
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
    with open(config_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    return json_data

def print_error(text: str):
    """Prints text in red"""
    print(Fore.RED + text + Style.RESET_ALL)
