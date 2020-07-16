from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Blog

class CreateAccountForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['name', 'email']

class CreatePenNameForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username']

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
