from django.contrib.auth import (get_user_model,
                                 authenticate,
                                 login as signin,
                                 logout as signout)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from colorama import Fore, Style
from datetime import date

from .forms import CreateAccountForm, CreatePenNameForm, BlogCreationForm
from .token import email_auth_token
from .models import Blog

def message(msg):
    print(Fore.MAGENTA, Style.BRIGHT, '\b\b[#]', Fore.RED, msg, Style.RESET_ALL)

def index(request):
    #return render(request, 'registration/confirm_to_msg.html')
    return render(request, 'app/index.html')

def logout(request):
    message(request.user.name + ' logged out.')
    signout(request)
    return redirect('/')

def login(request):
    err = {}
    #msg = 'Check your mail box and verify your mail id to continue'
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            signin(request, user)
            message(user.name + ' logged in.')
            return redirect('/blogs/view')
        err['err'] = 'Incorrect email or password. Make sure your email is verified (check your mailbox).'
        message('User not found.')
        if not email and not password:
            err['err'] = 'Provide a email and password to login'
        elif not email:
            err['err'] = 'Provide a email to login'
        elif not password:
            err['err'] = 'Incorrect password'
    return render(request, 'registration/login.html', err)



def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.name.capitalize()
            user.username = user.email
            user.is_active = False
            user.save()
            message(user.name + ' created an account.')
            ##### Sending Email verification mail #####
            site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = email_auth_token.make_token(user)
            link = 'http://{}/accounts/{}/{}'.format(site.domain, uid, token)
            email_subject = 'Confirm your account'
            mail = render_to_string('registration/confirm_mail.html', {'link':link, 'user':user})
            to_email = user.email
            email = EmailMessage(email_subject, mail, from_email='Key Blogs', to=[to_email])
            email.content_subtype = 'html'
            email.send()
            message('Email send to ' + user.name)
            ##########################################
            return redirect('/accounts/message/')
        message('Error in creating account')
        for field in form:
            for error in field.errors:
                message(field.label + ': ' + error)
    else:
        form = CreateAccountForm()
    return render(request, 'registration/create_account.html', {'form':form})


def post_create_account(request):
    return render(request, 'registration/confirm_to_msg.html')


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if request.method == 'POST' and user is not None:
        err = ''
        form = CreatePenNameForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.save()
            message(user.name + ' created a Pen Name.')
            signin(request, user)
            return redirect('/blogs/view/')
        message('Error in creating username for ' + user.name)
        for field in form:
            for error in field.errors:
                message(field.label + ': ' + error)
        err = 'Pen Name already taken'
        form = CreatePenNameForm()
        return render(request, 'registration/create_username.html', {'err':err})
    if user is not None and email_auth_token.check_token(user, token):
        user.is_active = True
        message(user.name + ' activated their account.')
        user.save()
        form = CreatePenNameForm()
        return render(request, 'registration/create_username.html', {'form':form})
    else:
        message('Invalid email verification link recieved.')
        return render(request, 'registration/confirm_failed.html')


@login_required
def view_account(request):
    return render(request, 'registration/view_account.html')


@login_required
def edit_account(request):
    return render(request, 'registration/edit_account.html')


@login_required
def edit_dp(request):
    return render(request, 'registration/edit_dp.html')


@login_required
def delete_account(request):
    msg = {}
    if request.method == 'POST':
        email = request.user.email
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            try:
                message(request.user.name + ' deleted their account.')
                get_user_model().objects.get(pk=request.user.id).delete()
                return redirect('/')
            except get_user_model().DoesNotExist:
                message('User not found')
                msg['err'] = 'User not found'
        else:
            msg['err'] = 'Incorrect Password'
    return render(request, 'registration/delete_account.html', msg)



@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = get_user_model().objects.get(pk=request.user.id)
            blog.pub_date = date.today()
            blog.mod_date = date.today()
            blog.save()
            message(request.user.name + ' created a new blog : ' + blog.title)
            return redirect('/blogs/view/')
        else:
            print(form.errors)
    else:
        form = BlogCreationForm()
    return render(request, 'app/create_blog.html', {'form':form})


@login_required
def view_blogs(request):
    blogs = Blog.objects.order_by('pub_date')
    return render(request, 'app/view_blogs.html', {'blogs':blogs})


@login_required
def view_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'app/view_blog.html', {'blog':blog})


@login_required
def view_blogger(request, pk):
    blogger = get_user_model().objects.get(pk=pk)
    return render(request, 'app/view_blogger.html', {'blogger':blogger})


@login_required
def edit_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    form = BlogCreationForm()
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.content = form.cleaned_data['content']
            blog.save()
            message(blog.author.name + " updated his blog '{}'".format(blog.title))
            return redirect('/accounts/view/')
    return render(request, 'app/edit_blog.html', {'blog':blog})


@login_required
def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        message(request.user.name + " deleted his blog '{}'".format(blog.title))
        blog.delete()
        return redirect('/accounts/view/')
    return render(request, 'app/delete_blog.html', {'blog':blog})


@login_required
def follow(request, pk):
    pass


@login_required
def unfollow(request, pk):
    pass


@login_required
def view_following(request):
    return render(request, 'app/following.html')


@login_required
def view_followers(request):
    return render(request, 'app/followers.html')