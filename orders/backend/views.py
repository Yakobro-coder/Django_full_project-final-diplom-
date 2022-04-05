from django.shortcuts import render


def home(request):
    return render(request, 'backend/home.html')


def log_in(request):
    return render(request, 'backend/log_in.html')


def sign_up(request):
    return render(request, 'backend/sign_up.html')
