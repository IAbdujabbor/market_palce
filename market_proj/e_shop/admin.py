from django.contrib import admin
from django.contrib import admin


from .models import *

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Conversation)
admin.site.register(ConversationMessage)

# Register your models here.
