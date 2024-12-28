from django.shortcuts import render

# Create your views here.
def index(request):
    friNames = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivan", "Julia"]
    context = {
        'names' : friNames
    }
    return render(request, 'subPractice/index.html', context)

def about(request):
    return render(request, "subPractice/about.html",{})