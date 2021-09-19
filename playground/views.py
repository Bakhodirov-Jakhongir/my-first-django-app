from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Something new request in django')

def sayHello(request):
    x = 1
    y = 2
    return render(request , 'index.html' , {'name' : 'Jakhongir'})
