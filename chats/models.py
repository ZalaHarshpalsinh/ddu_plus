from django.db import models
from authentication.models import *

# Create your models here.
class Message(models.Model):
    message = models.TextField(max_length=1000)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
