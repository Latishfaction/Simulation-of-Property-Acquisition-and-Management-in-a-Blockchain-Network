from django.db import models
from MuncipalCorporation_DB.models import Plot
# Create your models here.
class Complaint(models.Model):
    property_no = models.ForeignKey(Plot,on_delete=models.CASCADE,related_name="case_no")
