from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Something new request in django')

def calculate():
    x = 1
    return x

def sayHello(request):
    x = calculate()
    y = 2
    return render(request , 'index.html' , {'name' : 'Jakhongir'})
