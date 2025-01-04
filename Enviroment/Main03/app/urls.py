from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:linkSlug>/', views.rootLink , name='root-link'),
]