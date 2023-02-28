from django.db import models
from Aadhar_DB.models import aadhar
import datetime


# Create your models here.
class Person(models.Model):
    username = models.ForeignKey(aadhar, on_delete=models.CASCADE, related_name="user")
    password = models.CharField(max_length=30)
    otp = models.IntegerField(default=1111)
    date_joined = models.DateField(default=datetime.datetime.now())
    email = models.CharField(default="none",max_length=10)
    first_name = models.CharField(default="none",max_length=10)
    last_name = models.CharField(default="none",max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username.aadhar_no} => {self.username.first_name+' '+ self.username.last_name}"