from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: # declare which model the email field will interact with
        model = User # i.e. when we do form.save(), this is where we will save the data in the db
        fields = ['username', 'email', 'password1', 'password2'] # the fields we want shown on the form, and the order in which they are shown
