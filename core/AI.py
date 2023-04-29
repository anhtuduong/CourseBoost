import openai
import Logger as Logger

class AI:

    def __init__(self):
        
        self.name = None
        self.model = None
        self.api_key = None
        self.reply = None
        self.temperature = 1.0

    def set_name(self, name):
        self.name = name
        Logger.info(f"AI's name set to {self.name}")

    def set_model(self, model):
        self.model = model
        Logger.info(f"Model set to {self.model}")

    def set_api_key(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def set_temperature(self, temperature):
        self.temperature = temperature
        Logger.info(f"Temperature set to {self.temperature}")

    def chat(self, messages):
        chat = openai.ChatCompletion.create(
            model = self.model,
            messages = messages,
            temperature = self.temperature,
        )
        return chat

