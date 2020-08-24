from django.shortcuts import render
from .models import Recipe

# TO-DO - replace dummy homepage posts with widgets showing top posts from different categories
posts = [
{
    'author':'Author1',
    'title':'Post 1',
    'content':'content 1 here',
    'date_posted':'December 25 2019'
},
{
    'author':'Author2',
    'title':'Post 2',
    'content':'content 2 here',
    'date_posted':'August 10 2018'
}
]

def landing(request):
    return render(request, 'community/landing.html')

def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'community/home.html', context)

def recipes(request):
    context = {
    'posts': Recipe.objects.all(),
    'title': 'Recipes'
    }
    return render(request, 'community/recipes.html', context)

def fashion(request):
    return render(request, 'community/fashion.html')

def about(request):
    return render(request, 'community/about.html')
