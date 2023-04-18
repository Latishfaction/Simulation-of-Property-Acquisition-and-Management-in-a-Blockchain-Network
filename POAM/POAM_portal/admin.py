from django.contrib import admin
from .models import Person
from Aadhar_DB.models import User
# Register your models here.
admin.site.register(Person)
admin.site.register(User)
