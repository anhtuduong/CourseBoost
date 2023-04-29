import json

SECRET_FILE = '/home/toto/secrets.json'

def process_file():
    # Get API keys from file
    with open(SECRET_FILE, 'r') as f:
        secrets = json.load(f)
    return secrets

def get_openAI_key():
    secrets = process_file()
    return secrets['api_key']

def get_key_test():
    secrets = process_file()
    return secrets['api_key_test']

def get_django_key():
    secrets = process_file()
    return secrets['django_key']