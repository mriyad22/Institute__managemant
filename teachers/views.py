from django.shortcuts import render, redirect
from .forms import *
from .views import *
from django.contrib import messages


# Create your views here.

def tea_pro_update(request):
    try:
        user_data = request.user.teacher_profile
    except TeacherModel.DoesNotExist:
        user_data = None
    if request.method == "POST":
        form_data = TeacherProfileForm(request.POST, request.FILES, instance=user_data )
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.teacher = request.user
            data.save()
            messages.success(request, "Teacher Profile update successfully")
            return redirect("tea_profile")

    form_data = TeacherProfileForm(instance=user_data)
    con = {
        "data" : form_data,
        "title" : "teacher profile update",
        "btn" : "updata"
    }
            
    return render(request, "form.html", con)




def tea_profileview(request):

    return render(request, "profile.html")