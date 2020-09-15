'''
from django.db import models
from django.conf import settings

from blogs.models import Blog

class Chat(models.Model):
    messenger_1 = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='Messenger 1')
    messenger_2 = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='Messenger 2')

class Message(models.Model):
    chat = models.ForeignKey(Chat,
                             on_delete=models.CASCADE,
                             related_name='Chat')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='Sender')
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='Reciever')
    text = models.CharField('Message', max_length=60, blank=False, null=False)
    send_time = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    reciever = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='Reciever')
    writer_mentions = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.CASCADE,
                                        related_name='Mentioned Writer')
    blog_mentions = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Mentioned Blog')
    text = models.CharField('Message', max_length=200, blank=False, null=False)

'''
