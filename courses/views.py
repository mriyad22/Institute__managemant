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



#-------------> Course Model operation

def course_list(request):
    course = CourseModel.objects.all()

    con = {
        "data" : course,
        "title" : "courses"
    }

    return render(request, "crs/course_list.html", con)



def add_course(request):
    if request.method == "POST":
        form_data = CourseForm(request.POST, request.FILES)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.created_by = request.user
            data.save()
            messages.success(request, "Course uploaded")
            return redirect("course_list")

    form_data = CourseForm()
    con = {
        "data" : form_data,
        "title" : "add course",
        "btn" : "Upload"
    }

    return render(request, "form.html", con)




def edit_course(request, u_id):
    edit = get_object_or_404(CourseModel, id = u_id)

    if request.method == "POST":
        form_data = CourseForm(request.POST, request.FILES, instance=edit)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.created_by = request.user
            data.save()
            messages.success(request, "Course updated")
            return redirect("course_list")

    form_data = CourseForm(instance=edit)
    con = {
        "data" : form_data,
        "title" : "add course",
        "btn" : "Upload"
    }

    return render(request, "form.html", con)




def delete_course(request, d_id):
    delete_id = get_object_or_404(CourseModel, id = d_id)

    if request.method == "POST":
        delete_id.delete()
        messages.success(request, "Course Deleted")
        return redirect("course_list")

    con = {
        "object" : delete_id,
        "title" : "delete course"
    }

    return render(request, "delete.html", con)




def student_enroll(request):
    form_data = CourseEnrollmentForm()
    if request.method == "POST":
        form_data = CourseEnrollmentForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Student Enrolled")
            return redirect("student")

    con = {
        "data" : form_data,
        "title" : "Student Enroll",
        "btn" : "Enroll"
    }

    return render(request, "form.html", con)


def student_enroll_list(request):

    return render(request, "std/student.html")


def student_enroll_edit(request, pk):
    u_id = get_object_or_404(CourseEnrollmentModel, pk = pk)

    form_data = CourseEnrollmentForm(instance=u_id)
    form_data = CourseEnrollmentForm(instance=u_id)
    if request.method == "POST":
        form_data = CourseEnrollmentForm(request.POST,  instance=u_id)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Student Enroll updated")
            return redirect("student")

    con = {
        "data" : form_data,
        "title" : "Student Enroll update",
        "btn" : "Edit enroll"
    }

    return render(request, "form.html", con)



def Teacher_assign(request):
    if request.method == "POST":
        form_data = TeacherAssignForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Teacher Assigned")
            return redirect("teacher")

    form_data = TeacherAssignForm()
    con = {
        "data" : form_data,
        "title" : "Teacher assign",
        "btn" : "Assign"
    }

    return render(request, "form.html", con)



def Teacher_assign_update(request, pk):
    u_id = get_object_or_404(TeacherAssignModel, pk = pk)
    if request.method == "POST":
        form_data = TeacherAssignForm(request.POST, instance=u_id)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Teacher Assign updated")
            return redirect("teacher")

    form_data = TeacherAssignForm(instance=u_id)
    con = {
        "data" : form_data,
        "title" : "Teacher assign updated",
        "btn" : "Assign"
    }

    return render(request, "form.html", con)