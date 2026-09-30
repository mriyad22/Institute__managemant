from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .views import *
from django.contrib import messages

# Create your views here.
def teacher(request):
    return render(request, "tea/teacher.html", {"title" : "add teacher"})

def add_teacher(request):
    if request.method == "POST":
        form_data = TeacherProfileForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Teacher Profile update successfully")
            return redirect("all_tea_std")

    form_data = TeacherProfileForm()
    con = {
        "data" : form_data,
        "title" : "Create teacher profile",
        "btn" : "Create"
    }
            
    return render(request, "form.html", con)




def teacher_profile_update(request, u_id):
    update_id = TeacherModel.objects.get(id = u_id)
    if request.method == "POST":
        form_data = TeacherProfileUpdateForm(request.POST, request.FILES, instance=update_id)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Teacher Profile update successfully")
            return redirect("tea_profile")

    form_data = TeacherProfileUpdateForm(instance=update_id)
    con = {
        "data" : form_data,
        "title" : "teacher profile update",
        "btn" : "Update"
    }
            
    return render(request, "form.html", con)




def delete_student(request, pk):

    teacher = get_object_or_404(TeacherModel, pk=pk)

    if request.method == "POST":
        teacher.delete()
        return redirect("all_tea_std")

    context = {
        "object": teacher,
        "title" : f"delete id - {pk}"
    }

    return render(request, "delete.html", context)







def tea_profileview(request):

    return render(request, "profile.html")