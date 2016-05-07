from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    dict = {'boldmessage': "ou, i didn't see you"}
    return render(request, 'rango/index.html', context=dict)


def about(request):
    return render(request, 'rango/about.html')
