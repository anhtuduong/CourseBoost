import json

SECRET_FILE = '/home/toto/secrets.json'

class Key:

    def __init__(self) -> None:
        
        self.secrets = None

        # Get API keys from file
        with open(SECRET_FILE, 'r') as f:
            self.secrets = json.load(f)

    def get_openAI_key(self):
        return self.secrets['api_key']
    
    def get_key_test(self):
        return self.secrets['api_key_test']
    
    def get_django_key(self):
        return self.secrets['django_key']