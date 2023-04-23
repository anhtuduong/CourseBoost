import openai
from src.Key import Key
from src.InfoManager import InfoManager

EXIT_VALUE = 'exit'

openai.api_key = Key().get_openAI_key()

class Chat:

    def __init__(self) -> None:

        self.messages = [
            {"role": "system", "content": "You are a kind helpful assistant."},
        ]

        self.model = "gpt-3.5-turbo"
        self.message = ""

    def start(self):

        while self.message != EXIT_VALUE:
            self.message = input("User : ")
            
            if self.message == EXIT_VALUE:
                break

            if self.message:
                self.messages.append(
                    {"role": "user", "content": self.message},
                )
                self.chat = openai.ChatCompletion.create(
                    model = self.model,
                    messages = self.messages,
                    temperature = 1.0,
                )
            
            reply = self.chat.choices[0].message.content

            print(f"\nChatGPT: {reply}\n")

            self.messages.append({"role": "assistant", "content": reply})

        InfoManager.export(self.messages, self.chat)

            


            


            

# ------------------------------
if __name__ == "__main__":
    chat = Chat()
    chat.start()