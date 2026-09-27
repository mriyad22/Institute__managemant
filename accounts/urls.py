from django.urls import path
from .views import *

urlpatterns = [
    path("login/", loginview, name="login"),
    path("", dashboardveiew, name="dashboard"),
    path("logout/", loginview, name="logout"),
]
