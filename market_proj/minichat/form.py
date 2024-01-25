from django import forms

from minichat.models import ChatMessage


class ChatForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('content',)

    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))