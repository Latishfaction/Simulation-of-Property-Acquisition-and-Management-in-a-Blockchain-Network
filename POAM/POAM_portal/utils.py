"""
Code Utility functions which supports the views.py
-> Contains additional functions to provide better code readability and mantainence.
"""
from Aadhar_DB.models import aadhar, User
from .models import Person
from MuncipalCorporation_DB.models import Plot


# checking if the entered aadhar no. exits in the Aadhar_DB or not
# if found then create USER and show suceess status, else show not found status
def SameAadhar(username):
    try:
        print("Checking")
        if(str(username) =='latish'):
            print("Found")
            return False
        aadhari = aadhar.objects.get(aadhar_no=username)
        person_aadhar = Person.objects.get(aadhar_details=aadhari)
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


def get_person_info(aadhar_info):
    return Person.objects.get(aadhar_details=aadhar_info)


# return aadhar details from aadhar number
def get_aadhar_info(aadhar_no):
    return aadhar.objects.get(aadhar_no=aadhar_no)


def get_aadhar(aadhar_no):
    aadhar_info = get_aadhar_info(aadhar_no)
    person_info = get_person_info(aadhar_info)
    return person_info


def get_plot_withAadhar(aadhar_card):
    aadhar_info = get_aadhar_info(aadhar_card)
    person_info = get_person_info(aadhar_info)
    plot = Plot.objects.filter(owner=person_info)
    return plot

def get_plot_withPlotno(plot_no):
    plot_details = Plot.objects.get(number=plot_no)
    return plot_details