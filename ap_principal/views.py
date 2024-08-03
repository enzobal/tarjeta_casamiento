
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cbu(request):
    return render(request, 'cbu.html')
