from django.shortcuts import render, redirect
from .models import Post
from .forms import UserRegisterForm, PostForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            user = authenticate(
                username=username,
                password=password
            )
            login(request=request, user=user)
            return redirect("home")


    else:
        form = UserRegisterForm()

    return render(
                request=request,
                template_name="blog/register.html",
                context={"form": form})

def home(request):
    return render(request=request, template_name="blog/home.html")

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(
                request=request,
                template_name="blog/post_form.html",
                context={"form": form}
                )

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                username=username,
                password=password
            )
            if user is not None:
                login(request=request, user=user)
                return redirect("home")
    else:
        form = UserLoginForm()
    return render(request=request, template_name="blog/login.html", context={"form": form})

def user_logout(request):
    logout(request)
    return redirect("home")