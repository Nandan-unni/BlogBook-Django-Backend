from django.shortcuts import render, redirect

def handler404(request, *args, **argv):
    response = redirect('https://keyblogs.web.app/')

def index(request):
    return redirect('https://keyblogs.web.app/')
