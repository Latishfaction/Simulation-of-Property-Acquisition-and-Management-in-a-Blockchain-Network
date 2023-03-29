"""
Code Utility functions which supports the views.py
-> Contains additional functions to provide better code readability and mantainence.
"""
from Aadhar_DB.models import aadhar, User
from .models import Person


# checking if the entered aadhar no. exits in the Aadhar_DB or not
# if found then create USER and show suceess status, else show not found status
def SameAadhar(username):
    try:
        print("Hello", username)
        aadhar = aadhar.objects.get(aadhar_no=username)
        person_aadhar = Person.objects.get(aadhar_details=aadhar)
        return True
    except:
        return False


# Check for already registered entry on POAM_portal
def Duplicate(username):
    try:
        user = User.objects.get(username=username)
        person_user = Person.objects.get(user=user)
        print(user)
        return True
    except:
        return False
