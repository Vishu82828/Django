from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import JobBoard

# Create your views here.
def index(request):
    # job_posting = JobBoard.objects.all() filter(is_active=True)
    job_active = JobBoard.objects.all()
    context = {
        'job_post' : job_active
    }
    return render(request, 'job_board/index.html', context)

def jobDetail(req, id):
    # job_posting = JobBoard.objects.get(id=id)
    job_posting = get_object_or_404(JobBoard, id=id, is_active = True)
    context = {
        "job_details" : job_posting
    }
    return render(req, "job_board/details.html", context)