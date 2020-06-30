from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Writer, Blog

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2']

class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['gender']

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['dp', ]

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'tag']
