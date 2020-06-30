from django.shortcuts import render, redirect
from .forms import UserForm, WriterForm, BlogCreationForm
from .models import User, Blog
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from datetime import date

def index(request):
    return render(request, 'key_blogs/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        writerform = WriterForm(request.POST)
        if form.is_valid() and writerform.is_valid():
            user = form.save()
            writer = writerform.save(commit=False)
            writer.user = user
            writer.save()
            login(request, user)
            return redirect('/feeds/')
        else:
            print('Error in signup')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def feeds(request):
    blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'key_blogs/feeds.html', {'blogs':blogs})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            print(request.user)
            print(request.user.id)
            blog.author = User.objects.get(pk=request.user.id)
            blog.pub_date = date.today()
            blog.mod_date = date.today()
            blog.save()
            return redirect('/feeds/')
        else:
            print(form.errors)
    else:
        form = BlogCreationForm()
    return render(request, 'key_blogs/create.html', {'form':form})
