import os
import json

CHAT_LOG_FILE = 'chat_log/chats.json'
USAGE_LOG_FILE = 'chat_log/usage.json'

class InfoManager:
    
    def export(messages, chat):
        
        # check if output file exists
        if not os.path.exists(CHAT_LOG_FILE):
            with open(CHAT_LOG_FILE, 'w') as f:
                json.dump([], f, indent=4)

        # format data
        data = {
            "object": chat.object,
            "created": chat.created,
            "model": chat.model,
            "usage": chat.usage,
            "messages": messages
        }

        # load file and append data into it
        with open(CHAT_LOG_FILE, 'r') as f:
            file = json.load(f)
            file.append(data)
        with open(CHAT_LOG_FILE, 'w') as f:
            json.dump(file, f, indent=4)

        update_usage(chat.usage)

def update_usage(usage):

    # check if output file exists
    if not os.path.exists(USAGE_LOG_FILE):
        with open(USAGE_LOG_FILE, 'w') as f:
            json.dump({}, f, indent=4)

    # load current usage
    with open(USAGE_LOG_FILE, 'r') as f:
        current_usage = json.load(f)

    # update current usage
    current_usage['prompt_tokens'] += usage['prompt_tokens']
    current_usage['completion_tokens'] += usage['completion_tokens']
    current_usage['total_tokens'] += usage['total_tokens']

    # save current usage
    with open(USAGE_LOG_FILE, 'w') as f:
        json.dump(current_usage, f, indent=4)