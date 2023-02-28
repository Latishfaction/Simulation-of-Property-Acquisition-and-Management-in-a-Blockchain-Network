from django.urls import path
from . import views

urlpatterns=[
    path("path",views.pass,name=""),
]