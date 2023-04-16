import json

KEY_FILE = '/home/toto/secrets.json'

class APIKey:

    def __init__(self) -> None:
        
        self.secrets = None

        # Get API keys from file
        with open(KEY_FILE, 'r') as f:
            self.secrets = json.load(f)

    def getKey(self):
        return self.secrets['api_key']
    
    def getKeyTest(self):
        return self.secrets['api_key_test']