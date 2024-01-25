# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name', 'description', 'image', 'price']
        widgets = {
            'category': forms.Select(attrs={'class': 'select'}),
            'name': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'image': forms.FileInput(attrs={'class': 'file'}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # email = forms.CharField(label="Your name", max_length=100,)

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={'class': 'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))





class ItemEditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'image', 'price','category']

        def __init__(self, *args, **kwargs):
            super(ItemEditForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


        widgets = {
            'category': forms.Select(attrs={'class': 'select'}),
            'name': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'textarea'}),
            'image': forms.FileInput(attrs={'class': 'file'}),
            'price': forms.NumberInput(attrs={'class': 'input'}),
        }


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'input'})
        }