from django.urls import path
from .views import *


urlpatterns = [
    path("tea-pro-update/", tea_pro_update, name="tea_pro_update"),
    path("tea-profile/", tea_profileview, name="tea_profile"),
]
