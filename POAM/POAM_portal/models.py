from django.db import models
from Aadhar_DB.models import aadhar,User
import datetime
from django.db import models

# # Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    aadhar_details = models.ForeignKey(aadhar,on_delete=models.CASCADE,related_name="aadhar_user")
    

    def __str__(self):
        return f"{self.aadhar_details.aadhar_no} {self.aadhar_details.first_name}"

