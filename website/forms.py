from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name=forms.CharField(max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(max_length=100,label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
