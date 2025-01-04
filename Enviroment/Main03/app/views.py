from django.shortcuts import render, get_object_or_404, redirect
from .models import Link

# Create your views here.
def index(req):
    links = Link.objects.all()
    context = {
        "Links" : links
    }
    return render(req, 'app/index.html', context)

def rootLink(req, linkSlug):
    link = get_object_or_404(Link, slug=linkSlug)
    link.click()

    return redirect(link.url)