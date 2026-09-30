from django.db import models
from accounts.models import AuthUserModel

class CourseCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"





class CourseModel(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    category = models.ForeignKey(
        CourseCategoryModel,
        on_delete=models.SET_NULL,
        related_name="course_category",
        null = True
    )
    course_fee = models.FloatField(null=True)
    course_module = models.TextField()
    course_thumbnail = models.ImageField(upload_to="media/course_thum", null=True)
    credit = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        AuthUserModel,
        on_delete=models.SET_NULL,
        related_name="course_creator",
        null=True
    )

    def __str__(self):
        return f"{self.title}"