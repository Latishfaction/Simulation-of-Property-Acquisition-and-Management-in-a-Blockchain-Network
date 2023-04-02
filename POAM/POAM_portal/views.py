from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

# Create your views here.
from .models import Person
from .utils import *

# from .models import Person

# register the person from aadhar_db to POAM_portal
# authentication/views.py


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = "Deafult@test.com"
        user = authenticate(
            username=username,
            password=password,
        )
        if user is not None:
            if not SameAadhar(user.username):
                login(request, user)
                message = f"Hello {user}! You have been logged in"
                # return render(request, "POAM_portal/home.html", {"message": message})
                return HttpResponseRedirect(reverse("home", kwargs={"user": user}))
            else:
                return HttpResponse(SameAadhar(user))

        else:
            return HttpResponseRedirect(reverse("status", kwargs={"status": 0}))
    else:
        return render(
            request,
            "POAM_portal/login.html",
        )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        cpassword = request.POST["confirmpassword"]
        email = request.POST["email"]
        # checking password and conform-password
        if password != cpassword:
            return render(
                request,
                "POAM_portal/register.html",
                {
                    "message": "Passwords must match.",
                },
            )
        # validate double registration
        if Duplicate(username):
            return render(
                request,
                "POAM_portal/register.html",
                {
                    "message": "User Already Exists.",
                },
            )
        else:
            if SameAadhar(username):
                return HttpResponseRedirect(reverse("status", kwargs={"status": 1}))
            else:
                return HttpResponseRedirect(reverse("status", kwargs={"status": 0}))

    else:
        return render(request, "POAM_portal/register.html")


def success_status(request, status):
    if status == 0:
        link = "https://em-content.zobj.net/source/microsoft-teams/337/dizzy-face_1f635.png"
    else:
        link = (
            "https://em-content.zobj.net/source/microsoft-teams/337/thumbs-up_1f44d.png"
        )
    return render(
        request,
        "POAM_portal/status.html",
        {
            "status": status,
            "link": link,
        },
    )


@login_required(login_url="login")
def home_view(request, user):
    message = f"Hello {user}! You have been logged in"
    try:
        user_details = get_aadhar(user)
        return render(
            request,
            "POAM_portal/home.html",
            {
                "person": user_details.aadhar_details,
                "plots": get_plot(user),
            },
        )
    except:
        return HttpResponseRedirect(reverse("status", kwargs={"status": 0}))


@login_required(login_url="login")
def share_property(request):
    return render(request, "POAM_portal/share_property.html")


def bank(request):
    return render(request, "POAM_portal/bank.html")
