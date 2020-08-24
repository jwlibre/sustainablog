from django.shortcuts import render

def home(request):
    return render(request, 'master/home.html')

def about(request):
    return render(request, 'master/about.html')
