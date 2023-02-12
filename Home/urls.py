from django.urls import path
from .import views


urlpatterns = [
    path('',views.homescreen,name="homescreen"),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name='signout'),
    
    path('donate',views.donate,name='donate'),
    path('home',views.home,name='home'),
    path("OrganasationHome",views.OrganasationHome,name="OrganasationHome"),
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("UserConfirm",views.UserConfirm,name="UserConfirm"),
    path("OrgRegister",views.OrgRegister,name="OrgRegister"),
    path("DonnerConfirm",views.DonnerConfirm,name="DonnerConfirm"),
    
]
