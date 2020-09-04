from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-field'}))

    class Meta: # declare which model the email field will interact with
        model = User # i.e. when we do form.save(), this is where we will save the data in the db
        fields = ['username', 'email', 'password1', 'password2'] # the fields we want shown on the form, and the order in which they are shown

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match!")
    #
    #     return password2


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: # declare which model the email field will interact with
        model = User # i.e. when we do form.save(), this is where we will save the data in the db
        fields = ['username', 'email'] # the fields we want shown on the form, and the order in which they are shown

class ProfileUpdateForm(forms.ModelForm):
    class Meta: # declare which model the email field will interact with
        model = Profile # i.e. when we do form.save(), this is where we will save the data in the db
        fields = ['image'] # the fields we want shown on the form, and the order in which they are shown
