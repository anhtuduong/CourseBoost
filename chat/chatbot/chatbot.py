def chatbot(input_text):
    return "You said: " + input_text

import random

def get_bot_response(user_input):
    # Define a list of responses for the bot
    responses = [
        "Hello, how can I assist you today?",
        "I'm sorry, I didn't understand your request. Can you please rephrase it?",
        "Please provide more details so I can better understand your request.",
        "Thank you for reaching out. A member of our team will get back to you as soon as possible."
    ]
    
    # Generate a random response from the list
    bot_response = random.choice(responses)
    
    return bot_response
