from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

# FUNCTION-BASED VIEW
def landing(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('home')
    else:
        context = {
        'form': AuthenticationForm()
        }
        return render(request, 'community/landing.html', context)

def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'community/home.html', context)

# CLASS-BASED VIEW
def recipes(request):
    context = {
    'posts': Recipe.objects.all(),
    'title': 'Recipes'
    }
    return render(request, 'community/recipes.html', context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'community/recipes.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class RecipeDetailView(DetailView): # For individual recipes
    model = Recipe
    # By convention, django looks for a template with the naming convention:
    # <app>/<model>_<viewtype>.html
    # in this case, it will seek community/recipe_detail.html

class RecipeCreateView(LoginRequiredMixin, CreateView): # For individual recipes
    # need to use the login mixin because you can't use decorators on classes (so we can't put @login_required there!)
    model = Recipe
    fields = ['title', 'intro_paragraph', 'ingredients', 'method']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # run the form_valid method of the parent class
    # By convention, django looks for a template with the naming convention:
    # <app>/<model>_form.html
    # for both Create and Update functionality

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # For individual recipes
    # need to use the login mixin because you can't use decorators on classes (so we can't put @login_required there!)
    model = Recipe
    fields = ['title', 'intro_paragraph', 'ingredients', 'method']

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        else:
            return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) # run the form_valid method of the parent class
    # By convention, django looks for a template with the naming convention:
    # <app>/<model>_form.html
    # for both Create and Update functionality

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # For individual recipes
    model = Recipe
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        else:
            return False
    success_url = '/recipes'

def fashion(request):
    return render(request, 'community/fashion.html')

def about(request):
    return render(request, 'community/about.html')
