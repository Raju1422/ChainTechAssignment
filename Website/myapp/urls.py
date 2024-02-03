from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name='home'),
    path("signup/",views.register,name="signup"),
    path("login/",views.loginView,name="login"),
    path("logout/",views.logoutView,name="logout"),
    path("user-details/",views.userDetailsView,name="user-details"),
    path("users-list/",views.listOfUsers,name='user-list')
]