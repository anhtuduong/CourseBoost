import openai
from src.APIKey import APIKey

openai.api_key = APIKey().getKeys()

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"\nChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})