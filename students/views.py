from django.shortcuts import render, redirect 
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.

def student_profile(request):
    if not request.user.is_authenticated or request.user.user_type == "Student":
        messages.warning(request, "You don't have permision here!")
        return redirect("dashboard")

    try:
        user_data = request.user.student_profile
    except StudentModel.DoesNotExist:
        user_data = None
    if request.method == "POST":
        form_data = StudentProfileForm(request.POST, request.FILES, instance=user_data )
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.student = request.user
            data.save()
            messages.success(request, "Student Profile update successfully")
            return redirect("std_profile")

    form_data = StudentProfileForm(instance=user_data) 
    con = {
        "data" : form_data,
        "title" : " student profile update", 
        "btn" : "Update"
    }
    return render(request, "form.html", con)




def profileview(request):

    return render(request, "profile.html")
