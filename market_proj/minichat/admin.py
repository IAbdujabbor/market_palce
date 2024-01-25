from django.contrib import admin

from minichat.models import Chat, ChatMessage

# Register your models here.
admin.site.register(Chat)
admin.site.register(ChatMessage)
