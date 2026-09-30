from django.urls import path
from .views import *


urlpatterns = [
    #---------> course category urls
    path("add-course-category/", add_course_category, name="add_course_category"),
    path("edit-course-category/<int:u_id>/", edit_course_category, name="update_course_category"),
    path("course-category/", course_category_list, name='course_category_list'),
    path("delete-ourse-category/<int:d_id>/", delete_course_category, name="delete_course_category"),

    #-----------> course urls

    path("add-course/",add_course, name="add_course"),
    path("courses/", course_list, name="course_list"),
    path("edit-course/<int:u_id>/", edit_course, name="edit_course"),
    path("delete-course/<int:d_id>/", delete_course, name="delete_course"),
]
