
from django.shortcuts import render
from django.db.models import Q
from authentication.models import *
from chats.models import *

# Create your views here.
def landingPage(request):
    return render(request, 'landing_page.html')

def home(request):
    interlocutors = []

    messages = Message.objects.filter(Q(sender=request.user) | Q(receiver=request.user))

    for message in messages:
        if message.sender == request.user:
            person = message.receiver
        else:
            person = message.sender
        
        if person not in interlocutors:
            interlocutors += [person]
    
    return render(request ,'home.html', {
        'interlocutors':interlocutors,
    })