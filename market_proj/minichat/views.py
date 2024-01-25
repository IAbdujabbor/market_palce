from django.shortcuts import render

from minichat.form import ChatForm


# Create your views here.


def chat_view(request):
    form = ChatForm()
    return render(request, 'chat.html', {'form': form})