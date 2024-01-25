from django.urls import path

from minichat import views

urlpatterns = [
    path('chat/',views.chat_view, name="chat_view" ),

    # ... Add more URL patterns here ...
]