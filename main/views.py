from django.shortcuts import render
from django.http import HttpResponse

def aboutMe(request):
    return render(request, 'main/about.html')

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def showChess(request):
    return render(request, 'main/chess.html')

def showLanguages(request):
    return render(request, 'main/languages.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')