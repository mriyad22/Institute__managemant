from django.urls import path
from .views import *

urlpatterns = [
    path("student/", studentview, name="student"),
    path("add-student/", student_profile, name="add_student"),
    path("std-profile/", profileview, name="std_profile"),
    path("std-pro-update/<int:u_id>/", student_profile_update, name="student_update"),
    path("std-delete/<int:d_id>/", student_profile_delete, name="std_delete"),

]
