from src.AI import AI
from src.Prompt import Prompt
import src.Key as Key
from src.InfoManager import InfoManager
import src.Logger as Logger

EXIT_VALUE = 'exit'

class Chat:

    def __init__(self) -> None:

        self.chatgpt = AI()
        self.set_name("AI")
        self.set_model("gpt-3.5-turbo")
        self.set_api_key(Key.get_openAI_key())

        self.messages = [
            self.set_message("system", "You are a kind helpful assistant."),
        ]

    def start(self):

        Logger.debug("Chat started\n")
        message = ""
        while message != EXIT_VALUE:
            message = input("User : ")
            
            if message == EXIT_VALUE or not message:
                break

            self.messages.append(
                self.set_message("user", message),
            )

            chat = self.chat(self.messages)
            reply = self.get_reply(chat)

            print(f"\n{self.chatgpt.name}: {reply}\n")

            self.messages.append(
                self.set_message("assistant", reply)
            )

        Logger.debug("Chat ended")
        InfoManager.export(self.messages, chat)

    def set_name(self, name):
        self.chatgpt.set_name(name)

    def set_model(self, model):
        self.chatgpt.set_model(model)

    def set_api_key(self, api_key):
        self.chatgpt.set_api_key(api_key)

    def set_message(self, role, content):
        return {"role": role, "content": content}
    
    def chat(self, messages):
        return self.chatgpt.chat(messages)
    
    def get_reply(self, chat):
        return chat.choices[0].message.content
    
       

# ------------------------------
if __name__ == "__main__":
    chat = Chat()
    chat.start()