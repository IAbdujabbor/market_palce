
from e_shop.models import Item
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    item = models.ForeignKey(Item, related_name='chats', on_delete=models.CASCADE)
    users =  models.ManyToManyField(User, related_name='chats')
    created_at =models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =('-modified_at',)

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat,related_name='messages',on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User , related_name = "created_messages", on_delete=models.CASCADE)
    

   # modified_at



