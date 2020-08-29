"""sustainability_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views # alternative method to the include and creating a separate urls.py in each app
from community import views as community_views
from community.views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView,
    RecipeDeleteView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', community_views.landing, name='community-landing'),
    path('home/', community_views.home, name='community-home'),
    # path('recipes/', community_views.recipes, name='community-recipes'),
    path('recipes/', RecipeListView.as_view(), name='community-recipes'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='community-recipe-detail'),
    path('recipes/new/', RecipeCreateView.as_view(), name='community-recipe-create'),
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name='community-recipe-update'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='community-recipe-delete'),
    path('fashion/', community_views.fashion, name='community-fashion'),
    path('about/', community_views.about, name='community-about'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # FOR HOSTING STATIC UPLOADS IN DEV ONLY!
