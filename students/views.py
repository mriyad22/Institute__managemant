from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def studentview(request):

    return render(request, "std/student.html")


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
        "title" : " student profile", 
        "btn" : "Update"
    }
    return render(request, "form.html", con)



def student_profile_update(request, u_id):
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
    update_id = StudentModel.objects.get(id = d_id)
    update_id.delete()
    messages.success(request, "Student deleted")
    return redirect("all_tea_std")




def profileview(request):

    return render(request, "profile.html")
