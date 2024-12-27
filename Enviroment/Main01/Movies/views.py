from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies':['tarjan','dil-jale', 'ravan', 'water']
    }
    return render(request, 'Movies/index.html', context)

def about(request):
    return render(request,'Movies/about.html',{})