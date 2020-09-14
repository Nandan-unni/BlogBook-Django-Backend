'''
from django.db import models
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Sender')
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Reciever')
    text = models.CharField('Message', max_length=60, blank=False, null=False)
    send_time = models.DateTimeField(auto_now_add=True)
'''
