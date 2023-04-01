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
        aadhari = aadhar.objects.get(aadhar_no=username)
        person_aadhar = Person.objects.get(aadhar_details=aadhari)
        return False
    except:
        return True


# Check for already registered entry on POAM_portal
def Duplicate(username):
    try:
        user = User.objects.get(username=username)
        person_user = Person.objects.get(user=user)
        print(user)
        return True
    except:
        return False


# return aadhar details from aadhar number
def get_aadhar(aadhar_no):
    aadhar_info = aadhar.objects.get(aadhar_no=aadhar_no)
    person_aadhar = Person.objects.get(aadhar_details=aadhar_info)
    return person_aadhar
