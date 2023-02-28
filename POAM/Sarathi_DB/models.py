from django.db import models
from MuncipalCorporation_DB.models import Plot
from LegalComplaints_DB.models import Complaint
# Create your models here.

class Plot_details(models.Model):
    details = models.ForeignKey(Plot,related_name="plot_details",on_delete=models.CASCADE)

    def __str__(self):
        return f"{details.number} | {details.owner}"

class blacklist(models.Model):
    Property_case = models.ForeignKey(Complaint,on_delete=models.CASCADE,related_name="proprty_case")
    is_blocked = models.BooleanField(default=False)
