from django.urls import path
from .import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.LinkListView.as_view(), name='link-list'),
]