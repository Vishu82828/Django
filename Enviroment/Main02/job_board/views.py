from django.shortcuts import render, HttpResponse

from .models import JobBoard

# Create your views here.
def index(request):
    # job_posting = JobBoard.objects.all() filter(is_active=True)
    job_active = JobBoard.objects.all()
    context = {
        'job_post' : job_active
    }
    return render(request, 'job_board/index.html', context)