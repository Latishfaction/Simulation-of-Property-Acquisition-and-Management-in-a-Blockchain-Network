from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello")

# for temporary query of data base
# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "Aadhar_DB/login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "Aadhar_DB/login.html")


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("index"))


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         # email = request.POST["email"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(request, "Aadhar_DB/register.html", {
#                 "message": "Passwords must match."
#             })
#         otp = request.POST["otp"]
#         u1 = aadhar.objects.get(aadhar_no=username)
#         # Attempt to create new user
#         try:
#             user = User(username = u1, password = password,otp=otp)
#             # user.save()
#             print(user)
#         except IntegrityError:
#             return render(request, "Aadhar_DB/register.html", {
#                 "message": "Username already taken."
#             })
#         # login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "Aadhar_DB/register.html")

# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(request, "Aadhar_DB/register.html", {
#                 "message": "Passwords must match."
#             })
#         otp = request.POST["otp"]
#         # get the aadhar card by the username
#         u1 = aadhar.objects.get(aadhar_no = int(username))

#         print(u1)
#         # put the aadhar card data in the user model
#         try :
#             user = Person(username=u1,password=password,otp=otp)
#             user.save()
#             print("Saved")
#         except IntegrityError:
#             return render(request, "Aadhar_DB/register.html", {
#                 "message": "Username already taken."
#             })

#         return HttpResponse("Done")
#     else:
#         return render(request,"Aadhar_DB/register.html")
