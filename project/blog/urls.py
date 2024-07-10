from django.urls import path
from . import views

urlpatterns:list = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logount/", views.user_logout, name="logout"),
    path("post/new/", views.create_post, name="create-post"),
    path("profile/", views.get_posts_user, name="profile"),
    path("post/<int:pk>/edit/", views.edit_post_user, name="edit_post")


]