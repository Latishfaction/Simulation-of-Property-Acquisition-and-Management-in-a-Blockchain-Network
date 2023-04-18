from django.db import models
from MuncipalCorporation_DB.models import Plot
from LegalComplaints_DB.models import Complaint
from POAM_portal.models import Person
# Create your models here.

class Plot_details(models.Model):
    details = models.ForeignKey(Plot,related_name="master_plot_details",on_delete=models.CASCADE)

    def __str__(self):
        return f"{details.number} | {details.owner}"

class blacklist(models.Model):
    Property_case = models.ForeignKey(Complaint,on_delete=models.CASCADE,related_name="proprty_case")
    is_blocked = models.BooleanField(default=False)

# chain of people
class chain_of_title(models.Model):
    plot = models.ForeignKey(Plot,on_delete=models.CASCADE,related_name="plot_owner_name",default=None)
    # year,month,day from datetime.date
    onwership_date = models.DateField()
    selling_date = models.DateField(null=True)

class plot_agreement(models.Model):
    purchaser = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="plot_purchaser")
    purchaser_sign = models.BooleanField(default=False)
    
    buyer = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="plot_buyer")
    buyer_sign = models.BooleanField(default=False)
    
    plot_details = models.ForeignKey(Plot,related_name="plot_details",on_delete=models.CASCADE)
    total_amount = models.BigIntegerField()
    agreement_duration = models.DateField()

    purchaser_witness = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="plot_purchaser_witness")
    purchaser_witness_sign = models.BooleanField(default=False)

    buyer_witness = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="plot_buyer_witness")
    purchaser_witness_sign = models.BooleanField(default=False)


class proxy_agreement(models.Model):
    proxy_agreement_details = models.ForeignKey(plot_agreement,on_delete=models.CASCADE,related_name="prxy_agrmnt")