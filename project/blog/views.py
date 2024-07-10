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
            password = form.cleaned_data.get("password1")
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
    posts = Post.objects.filter(is_publish=True)
    context = {"posts": posts}
    return render(request=request, template_name="blog/home.html", context=context)

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
                template_name="blog/create_post.html",
                context={"form": form}
                )

def user_login(request):
    if request.method == "POST":
        print(request.POST)
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

@login_required
def get_posts_user(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    return render(request=request, template_name="blog/profile.html", context={"posts": posts})

@login_required
def edit_post_user(request, pk):
    post = Post.objects.filter(id=pk).filter(author=request.user).first()
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('profile')
    elif request.method == "GET":
         form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})