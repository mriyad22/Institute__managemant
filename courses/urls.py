from django.urls import path
from .views import *


urlpatterns = [
    path("add-course-category/", add_course_category, name="add_course_category"),
    path("edit-course-category/<int:u_id>/", edit_course_category, name="update_course_category"),
    path("course-category-list/", course_category_list, name='course_category_list'),
    path("delete-ourse-category/<int:d_id>/", delete_course_category, name="delete_course_category")
]
