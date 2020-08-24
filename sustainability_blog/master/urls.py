from django.urls import path
from . import views # i.e. importing module views from within this directory

urlpatterns = [
    path('', views.home, name='master-home'),
    path('about', views.about, name='master-about'),
]
