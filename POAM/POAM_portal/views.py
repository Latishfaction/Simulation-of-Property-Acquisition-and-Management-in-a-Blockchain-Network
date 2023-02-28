from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from Aadhar_DB.models import aadhar
from .models import Person

#register the person from aadhar_db to POAM_portal
# authentication/views.py

from . import forms


def login_view(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            user = authenticate(
                username= username,
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username.first_name}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'POAM_portal/login.html', context={'form': form, 'message': message})

def logout_view(request):
    logout(request)
    return HttpResponse("Log out done!")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        # email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "POAM_portal/register.html", {
                "message": "Passwords must match."
            })
        u1 = aadhar.objects.get(aadhar_no=int(username))
        # Attempt to create new user
        try:
            user = Person(username = u1, password = password)
            for peoples in Person.objects.all():
                if peoples.username.aadhar_no == user.username.aadhar_no:
                    # print(peoples.username.aadhar_no == user.username.aadhar_no)
                    raise Exception

                    
            else:
                # print("save it not same")
                user.save()
        except (Exception):
            return render(request, "POAM_portal/register.html", {
                "message": "Username already taken."
            })
        # login(request, user)
        return HttpResponseRedirect(reverse("register"))
    else:
        return render(request, "POAM_portal/register.html")