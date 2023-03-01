from django.db import models
from Aadhar_DB.models import aadhar
import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     pass


# # Create your models here.
# class People(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
#     aadhar_details = models.ForeignKey(aadhar,on_delete=models.CASCADE,related_name="aadhar_user")
#     otp = models.IntegerField()