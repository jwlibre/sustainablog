from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # saves user to table, easy!
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully, you are now able to log in.')
            return redirect('login') #name given to url pattern for homepage
        else:
            messages.error(request, 'Error creating user.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
