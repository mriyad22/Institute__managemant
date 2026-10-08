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

    #To show user-friendly error, if same user in same course
    def clean(self):
        cleaned_data = super().clean()

        student = cleaned_data.get("student")
        course = cleaned_data.get("course")

        if student and course:
            if CourseEnrollmentModel.objects.filter(
                student = student,
                course = course
            ).exists():
                raise forms.ValidationError("Student already enrolled in course.")
        return cleaned_data




class TeacherAssignForm(forms.ModelForm):
    class Meta:
        model = TeacherAssignModel
        fields = "__all__"