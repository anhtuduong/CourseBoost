import os
import json
import src.Logger as Logger

CHAT_LOG_FILE = 'mastergpt/chat_log/chats.json'
USAGE_LOG_FILE = 'mastergpt/chat_log/usage.json'

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

        Logger.debug(f'Chat log exported to {CHAT_LOG_FILE}')

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
    current_usage['completion_tokens'] += usage['completion_tokens']
    current_usage['prompt_tokens'] += usage['prompt_tokens']
    current_usage['total_tokens'] += usage['total_tokens']

    # save current usage
    with open(USAGE_LOG_FILE, 'w') as f:
        json.dump(current_usage, f, indent=4)

    Logger.debug(f'Usage log updated to {USAGE_LOG_FILE}')
    Logger.info(f'completion_tokens: {usage.completion_tokens}')
    Logger.info(f'prompt_tokens: {usage.prompt_tokens}')
    Logger.info(f'total_tokens: {usage.total_tokens}')