from django.urls import path
from .views import *

urlpatterns = [
    path("std-pro-update/", student_profile, name="std_update_pro"),
    path("std-profile/", profileview, name="profile"),
]
