from django.urls import path
from .views import *


urlpatterns = [
    path("add_teacher/", add_teacher, name="add_teacher"),
    path("tea-profile/", tea_profileview, name="tea_profile"),
    path("teacher/", teacher, name="teacher"),

    path("delete/<int:d_id>/", delete_teacher, name="tea_delete"),
    path('tea-pro-up/<int:u_id>/', teacher_profile_update, name="tea_update"),
]
