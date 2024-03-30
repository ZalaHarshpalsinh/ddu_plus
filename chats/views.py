from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import JsonResponse
import pytz
import json
from .models import *

# Create your views here.
def sendMessage(request, user_id):
    if request.method == 'POST':
        if request.POST['message'] is not None:
            message = Message(message=request.POST['message'], sender=request.user , receiver=User.objects.get(id=user_id))
            message.save()
            return redirect('chats:displayChat', user_id)


def displayChat(request, user_id):
    
    interlocutor = User.objects.get(id=user_id)
    messages = Message.objects.filter(Q(sender=request.user, receiver=interlocutor) | Q(sender=interlocutor, receiver=request.user)).order_by('dateTime') 
    return render(request, 'chats/chat.html', {
        'interlocutor':interlocutor,
        'messages':messages,
    })

def fetchMessages(request, user_id):
    interlocutor = User.objects.get(id=user_id)
    messages = Message.objects.filter(Q(sender=request.user, receiver=interlocutor) | Q(sender=interlocutor, receiver=request.user)).order_by('dateTime') 
    messages_data = [
        {
            'message': message.message,
            'sender': message.sender.username,
            'receiver': message.receiver.username,
            'dateTime': message.dateTime.astimezone(pytz.timezone('Asia/Kolkata')).strftime('%d-%m-%Y %H:%M:%S'),
        }
        for message in messages
    ]
    return JsonResponse(messages_data, safe=False)
