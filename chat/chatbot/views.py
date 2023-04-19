from django.shortcuts import render
from django.http import JsonResponse
from .chatbot import get_bot_response
from .models import Chat

def home(request):
    if request.method == 'POST':
        message_text = request.POST.get('message', '')
        if message_text.strip() != '':
            message = Chat(user='user', text=message_text)
            message.save()
            bot_response_text = get_bot_response(message_text)
            bot_response = Chat(user='bot', text=bot_response_text)
            bot_response.save()

    messages = Chat.objects.all()

    return render(request, 'home.html', {'messages': messages})

def chat(request):
    if request.method == 'POST':
        message_text = request.POST.get('message', '')
        if message_text.strip() != '':
            bot_response_text = get_bot_response(message_text)
            bot_response = Chat(user='bot', text=bot_response_text)
            bot_response.save()
            response_data = {
                'user_message': message_text,
                'bot_response': bot_response_text
            }
            return JsonResponse(response_data)
    else:
        response_data = {'error': 'Invalid request method.'}
        return JsonResponse(response_data)
