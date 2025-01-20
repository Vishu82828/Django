from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Profile, Link

# Create your views here.
def index(req):
    return HttpResponse( "hello")

class LinkListView(ListView):
    model = Link

class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')
