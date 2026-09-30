from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *

def add_course_category(request):
    if request.method == "POST":
        form_data = CourseCategoryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Created a category")
            return redirect("course_category_list")
        
    form_data = CourseCategoryForm()
    con = {
        "data" : form_data,
        "title" : "add category",
        "btn" : "Add"
    }

    return render(request, "form.html", con)




def edit_course_category(request, u_id):
    edit_id = get_object_or_404(CourseCategoryModel, id = u_id)

    if request.method == "POST":
        form_data = CourseCategoryForm(request.POST, instance=edit_id)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "updated a category")
            return redirect("course_category_list")
        
    form_data = CourseCategoryForm(instance=edit_id)
    con = {
        "data" : form_data,
        "title" : "edit category",
        "btn" : "Update"
    }

    return render(request, "form.html", con)




def delete_course_category(request, d_id):
    delete_id = get_object_or_404(CourseCategoryModel, id = d_id)

    if request.method == "POST":
        delete_id.delete()
        messages.success(request, "Deleted a category")
        return redirect("course_category_list")
        
    con = {
        "data" : delete_id,
        "title" : "delete category"
    }

    return render(request, "delete.html", con)




def course_category_list(request):
    category = CourseCategoryModel.objects.all()

    con = {
        "data" : category,
        "title" : "course category",
    }

    return render(request, "crs/course_category_list.html", con)
