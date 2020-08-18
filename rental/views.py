from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html', { "title": "Welcome" })
    

def about(request):
    return render(request, 'about.html', { "title": "About me" })