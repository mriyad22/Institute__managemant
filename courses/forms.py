from django import forms
from .models import *


class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategoryModel
        fields = "__all__"



class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = "__all__"
        exclude = ["created_by", "updated_at", "created_at"]



class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollmentModel
        fields = "__all__"
        exclude = [
            "adminssion_fee",
            "due"
        ]


class TeacherAssignForm(forms.ModelForm):
    class Meta:
        model = TeacherAssignModel
        fields = "__all__"