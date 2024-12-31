from django.shortcuts import render
from .forms import SignUp
# Create your views here.
def index(request):
    return render(request, 'subPractice/index.html', {})

def about(request):
    return render(request, 'subPractice/about.html', {})

def service(req):
    return render(req, 'subPractice/service.html', {})

def signin(req):
    return render(req, 'subPractice/signin.html', {})

def signup(req):
    if req.method == 'POST':
        # form has data
        formData = SignUp()
        if formData.is_valid():
            # save the data
            formData.save()
    else:
        formData = SignUp()
    context = {
        "formData" : formData
    }
    return render(req, 'subPractice/signup.html', context)