from .models import *
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blogForm(ModelForm):
    class Meta:
        model=Blogs
        fields='__all__'
        exclude=['likes','date']
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']