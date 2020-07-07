from django.shortcuts import render, redirect
from .forms import UserForm, WriterForm, BlogCreationForm, ProfilePicForm
from .models import User, Blog, Like, Writer
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from datetime import date
from django.http import HttpResponse
from colorama import Fore, Style

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
            print(Fore.RED, 'New User Created: {}'.format(user.first_name), Style.RESET_ALL)
            login(request, user)
            return redirect('/feeds/')
        else:
            print('Error in signup')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def profile_view(request):
    return render(request, 'key_blogs/profile.html')


@login_required
def feeds(request):
    blogs = Blog.objects.order_by('pub_date')
    return render(request, 'key_blogs/feeds.html', {'blogs':blogs})


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = User.objects.get(pk=request.user.id)
            blog.pub_date = date.today()
            blog.mod_date = date.today()
            blog.save()
            print(Fore.RED, 'New Blog Created: {}'.format(blog), Style.RESET_ALL)
            return redirect('/feeds/')
        else:
            print(form.errors)
    else:
        form = BlogCreationForm()
    return render(request, 'key_blogs/create.html', {'form':form})


@login_required
def like_blog(request, blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=blog_id)
        like = Like()
        like.liker = request.user
        like.ofblog = blog
        like.save()
        print(Fore.RED, "New Like by {} in '{}'".format(request.user, blog), Style.RESET_ALL)
    return redirect('/feeds/')

@login_required
def upload_dp(request):
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            writer = Writer.objects.get(user=user)
            writer.dp = form.cleaned_data['dp']
            writer.save()
            print(Fore.RED, 'Profile Pic updated: {}'.format(form.cleaned_data['dp']), Style.RESET_ALL)
            return redirect('/profile/')
        print(form.errors)
    else:
        form = ProfilePicForm()
    return render(request, 'key_blogs/profilepic.html', {'form':form})
