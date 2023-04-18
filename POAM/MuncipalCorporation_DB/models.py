from django.db import models
from POAM_portal.models import Person
# Create your models here.
class Plot(models.Model):
    SQFT = 'sqft'
    ACRE = 'AC'
    units = [
        (SQFT, 'Square.ft'),
        (ACRE, 'Acre'),
    ]
    owner = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="plot_owner",default=None)
    number = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    length= models.DecimalField(max_digits=10, decimal_places=2)
    width= models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(choices=units,default=SQFT,max_length=4)
    society_name= models.CharField(max_length=100)
    society_rera_no = models.IntegerField()
    plot_address = models.CharField(max_length=200)
    north = models.CharField(max_length=30)
    south = models.CharField(max_length=30)
    east = models.CharField(max_length=30)
    west = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.number} | {self.owner}"

class chain_of_title(models.Model):
    owner = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="owner_title_chain")
    plot = models.ForeignKey(Plot,on_delete=models.CASCADE,related_name="property_title_chain")
    # give result in datetime.date format
    ownership_date = models.DateField()
    selling_date = models.DateField(blank=True,null=True)