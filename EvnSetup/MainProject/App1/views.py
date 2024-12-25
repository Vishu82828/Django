from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("About Me")