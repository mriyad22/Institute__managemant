from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import *
from .models import *

from courses.models import CourseEnrollmentModel

# Create your views here.
def studentview(request):
    if request.user.user_type == "Admin":
        course_details = CourseEnrollmentModel.objects.all()
    elif request.user.user_type == "Student":
        course_details = CourseEnrollmentModel.objects.filter(student = request.user.student_profile)
    else:
        return redirect("dashboard")

    con = {
        "data" : course_details,
        "title" : "add student"
    }
    return render(request, "std/student.html", con)


def student_profile(request):
    # if not request.user.is_authenticated or request.user.user_type != "Student":
    #     messages.warning(request, "You don't have permision here!")
    #     return redirect("dashboard")

    if request.method == "POST":
        form_data = StudentProfileForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Student Profile update successfully")
            return redirect("std_profile")

    form_data = StudentProfileForm() 
    con = {
        "data" : form_data,
        "title" : "Create student profile", 
        "btn" : "Create"
    }
    return render(request, "form.html", con)



def student_profile_update(request, u_id):
    # try:
    #     update_id = request.user.student_profile
    # except StudentModel.DoesNotExist:
    #     update_id = None
    update_id = StudentModel.objects.get(id = u_id)
    if request.method == "POST":
        form_data = StudentProfileUpdateForm(request.POST, request.FILES, instance=update_id)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Student Profile update successfully")
            return redirect("std_profile")

    form_data = StudentProfileUpdateForm(instance=update_id) 
    con = {
        "data" : form_data,
        "title" : " student profile", 
        "btn" : "Update"
    }
    return render(request, "form.html", con)



def student_profile_delete(request, d_id):
    delete_id = StudentModel.objects.get(id = d_id)
    if request.method == "POST":
        delete_id.delete()
        messages.success(request, "Student deleted")
        return redirect("all_tea_std")

    con = {
        "object" : delete_id,
        "title" : "Delete Student"
    }

    return render(request, "delete.html", con)




def profileview(request):

    return render(request, "profile.html")