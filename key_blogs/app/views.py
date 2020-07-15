from django.contrib.auth import (get_user_model,
                                 authenticate,
                                 login as signin,
                                 logout as signout)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from colorama import Fore, Style

from .forms import CreateAccountForm, CreatePenNameForm
from .token import email_auth_token

def message(msg):
    print(Fore.MAGENTA, Style.BRIGHT, '\b\b[#]', Fore.RED, msg, Style.RESET_ALL)

def index(request):
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
        err['err'] = 'Incorrect email or password'
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
            message('New User created: ' + user.name)
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
            return redirect('/login/')
        message('Error in creating account')
        for field in form:
            for error in field.errors:
                message(field.label + ': ' + error)
    else:
        form = CreateAccountForm()
    return render(request, 'registration/create_account.html', {'form':form})


def create_username(request):
    err = {}
    if request.method == 'POST':
        form = CreatePenNameForm(request.POST)
        if form.is_valid():
            user = get_user_model().objects.get(pk=request.user.id)
            user.username = form.cleaned_data['username']
            user.save()
        return redirect('/blogs/view/')
    return render(request, 'registration/create_username.html', err)


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
    return render(request, 'registration/delete_account.html')



@login_required
def create_blog(request):
    return render(request, 'app/create_blog.html')


@login_required
def view_blogs(request):
    return render(request, 'app/view_blogs.html')


@login_required
def edit_blog(request):
    return render(request, 'app/edit_blog.html')


@login_required
def delete_blog(request):
    return render(request, 'app/delete_blog.html')



@login_required
def view_following(request):
    return render(request, 'app/following.html')


@login_required
def view_followers(request):
    return render(request, 'app/followers.html')