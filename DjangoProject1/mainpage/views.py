from django.shortcuts import render


def index(request):
    return render(request, 'mainpage/index.html')


def about(request):
    return render(request, 'mainpage/about.html')
