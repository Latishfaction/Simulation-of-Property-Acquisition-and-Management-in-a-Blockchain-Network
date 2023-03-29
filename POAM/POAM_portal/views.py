from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

# Create your views here.
from .models import Person
from .utils import SameAadhar, Duplicate

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
            if SameAadhar(user):
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


# def login_view(request):
#     form = forms.LoginForm()
#     message = ""
#     if request.method == "POST":
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 message = f"Hello {user}! You have been logged in"
#             else:
#                 return HttpResponseRedirect(reverse("status", kwargs={"status": 0}))
#     return render(
#         request, "POAM_portal/login.html", context={"form": form, "message": message}
#     )


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


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = "Deafult@test.com"

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(
#                 request, "Aadhar_DB/register.html", {"message": "Passwords must match."}
#             )


#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             person = Person()
#             person.user = user
#             person.aadhar_details = aadhar.objects.get(aadhar_no=int(username))
#             user.save()
#             person.save()
#         except IntegrityError:
#             return render(
#                 request, "POAM_portal/register.html", {"message": "Already Registered."}
#             )
#         except Exception:
#             return render(
#                 request,
#                 "POAM_portal/register.html",
#                 {
#                     "message": Exception,
#                 },
#             )
#         login(request, user)
#         return HttpResponse("Registered and login successfully!")
#     else:
#         return render(request, "POAM_portal/register.html")
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
    return render(
        request,
        "POAM_portal/home.html",
        {
            "message": message,
        },
    )
