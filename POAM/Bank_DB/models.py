from django.db import models
from POAM_portal.models import Person
# Create your models here.

class Account(models.Model):
    acc_holder_name = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="acc_holder")
    acc_balance = models.IntegerField()

    def __str__(self):
        return self.acc_holder_name

class Transaction(models.Model):
    sender = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="sender")
    receiver = models.ForeignKey(Person,on_delete=models.CASCADE,related_name="receiver")
    amount = models.IntegerField()
    remarks = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.amount} from : {self.sender} to {self.receiver}"