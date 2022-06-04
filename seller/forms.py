from django import forms
from seller.models import Bikes

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BikeForm(forms.ModelForm):
    class Meta:
        model=Bikes
        fields="__all__"

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())