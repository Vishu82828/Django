from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello this is django")

def about(request):
    return HttpResponse("this is about me, vishu")

def hello(request, first_name):
    return HttpResponse(f"hello {first_name}")

def add(request, num1, num2):
    return HttpResponse(f'Total = {num1+num2}')

def name(req):
    return HttpResponse("hello pyush")