from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

# Create your views here.
from Aadhar_DB.models import aadhar, User
from .models import Person

# from .models import Person

# register the person from aadhar_db to POAM_portal
# authentication/views.py

from . import forms


def login_view(request):
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                message = f"Hello {user}! You have been logged in"
            else:
                message = "Login failed!"
    return render(
        request, "POAM_portal/login.html", context={"form": form, "message": message}
    )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("register"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = "Deafult@test.com"

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "Aadhar_DB/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            person = Person()
            person.user = user
            person.aadhar_details = aadhar.objects.get(aadhar_no=int(username))
            user.save()
            person.save()
        except IntegrityError:
            return render(
                request, "POAM_portal/register.html", {"message": "Already Registered."}
            )
        except Exception:
            return render(
                request,
                "POAM_portal/register.html",
                {
                    "message": Exception,
                },
            )
        login(request, user)
        return HttpResponse("Registered and login successfully!")
    else:
        return render(request, "POAM_portal/register.html")
