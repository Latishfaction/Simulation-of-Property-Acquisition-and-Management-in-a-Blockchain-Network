from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class aadhar(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'OTH'
    gender = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    ]
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(choices=gender,default=OTHERS,max_length=3)
    aadhar_no = models.BigIntegerField()
    address = models.TextField()
    photo = models.ImageField(upload_to ='uploads/',null=True)

    def __str__(self):
        return f"Aadhar No : {self.aadhar_no} DOB : {self.dob}"




    # password = models.password()