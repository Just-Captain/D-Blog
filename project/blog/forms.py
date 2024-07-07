from django import forms
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["title", "content", "is_publish"]
    