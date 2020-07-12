from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def feeds(request):
    return render(request, 'app/feeds.html')

def create_account(request):
    return render(request, 'registration/create_account.html')

def view_account(request):
    return render(request, 'registration/view_account.html')

def edit_account(request):
    return render(request, 'registration/edit_account.html')

def edit_dp(request):
    return render(request, 'registration/edit_dp.html')

def delete_account(request):
    return render(request, 'registration/delete_account.html')

def create_blog(request):
    return render(request, 'app/create_blog.html')

def edit_blog(request):
    return render(request, 'app/edit_blog.html')

def delete_blog(request):
    return render(request, 'app/delete_blog.html')

def view_following(request):
    return render(request, 'app/following.html')

def view_followers(request):
    return render(request, 'app/followers.html')