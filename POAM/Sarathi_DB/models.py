from django.db import models
from MuncipalCorporation_DB.models import Plot
# Create your models here.

class Plot_details(models.Model):
    details = models.ForeignKey(Plot,related_name="plot_details",on_delete=models.CASCADE)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{details.number} | {details.owner}"
