
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("postlike/<int:postid>",views.countpostlike, name="postlike"),
    path("allpost", views.allpost, name="allpost"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
