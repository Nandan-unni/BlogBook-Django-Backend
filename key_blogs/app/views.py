from django.contrib.auth import login as signin, authenticate, logout as signout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CreateAccountForm


def index(request):
    return render(request, 'app/index.html')

def logout(request):
    signout(request)
    return redirect('/')

def login(request):
    err = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        print(user)
        if user is not None:
            signin(request, user)
            print('Login success')
            return redirect('/blogs/view')
        err['err'] = 'Incorrect email or password'
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
            user.save()
            print('\nNew User created: ', user.name, '\n')
            return redirect('/blogs/view/')
        print('Error in creating account')
        for field in form:
            for error in field.errors:
                print(field.label, ': ', error)
    else:
        form = CreateAccountForm()
    return render(request, 'registration/create_account.html', {'form':form})


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