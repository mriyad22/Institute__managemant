from django.urls import path
from .views import *

urlpatterns = [
    path("register/", user_register_view, name="register"),
    path("login/", loginview, name="login_page"),
    path("", dashboardveiew, name="dashboard"),
    path("logout/", logoutview, name="logout_page"),
]
