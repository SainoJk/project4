from os import supports_dir_fd
from typing import SupportsIndex
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import PostLike, User,PostInfo


def index(request):
    if request.user.is_authenticated:
        spostmodel=PostInfo()
        if request.method == 'POST':
            print("create new post")
            spostmodel.spostuser=User(request.user.id)
            print(request.POST.get)
            spostmodel.spostinfo=request.POST.get("txtPost","")
            spostmodel.save()
            return HttpResponseRedirect(reverse("allpost")) 
        return render(request, "network/index.html")
    else:
        return login_view(request)


def countpostlike(request,postid):
    mpostid=PostInfo(postid)

    spostlike=PostLike()
    spostlike.spostid=mpostid
    spostlike.slikeuser=User(request.user.id)
    spostlike.save()

    icount = PostLike.objects.filter(spostid=mpostid).count()

    mpostInfo=PostInfo.objects.get(id=postid)
    mpostInfo.spostlike=icount
    mpostInfo.save()

    print(f"Count {icount}")
    return JsonResponse({"likecount": icount}, status=200)

def allpost(request):
    spostinfo=PostInfo.objects.all()
    return render(request, "network/allpost.html",{
        "postlists":spostinfo
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
