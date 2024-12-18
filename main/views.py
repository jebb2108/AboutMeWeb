from django.shortcuts import render
from django.http import HttpResponse

def aboutMe(request):
    return HttpResponse('<h2>My name`s Gabriel, and I`m 22 years old</h2>')

# Create your views here.
def index(request):
    return render(request, 'index.html')