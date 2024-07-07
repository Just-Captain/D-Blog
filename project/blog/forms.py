from django import forms
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["title", "content", "is_publish"]
    