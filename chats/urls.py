from django.urls import path,include
from . import views

app_name = 'chats'

urlpatterns = [
    path('send_message/<user_id>', views.sendMessage, name='sendMessage'),
    path('<user_id>', views.displayChat, name='displayChat'),
    path('messages/<user_id>', views.fetchMessages, name='fetchMessages'),
]