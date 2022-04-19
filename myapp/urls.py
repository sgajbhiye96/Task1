from django.urls import path,include
from . import views


# creating urls for registration ,login and home page.
urlpatterns = [
   path('',views.RegisterPage,name="registerpage"),
   path("register/",views.UserRegister,name="register"),
   path("loginpage/",views.LoginPage,name="loginpage"),
   path("loginuser/",views.LoginUser,name="login"),
   path("profile/",views.profile,name="profile")

]