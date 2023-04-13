from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("status/<int:status>", views.success_status, name="status"),
    path("home/<str:user>", views.home_view, name="home"),
    path("<str:user>/share", views.share_property, name="share"),
    path("home/<str:plot_no>/myproperties", views.my_properties, name="myproperty"),
    path("home/<str:plot_no>/shareProperty", views.SharedProperty_view, name="sharedproperty"),
    
    path("bank", views.bank, name="bank"),
]
