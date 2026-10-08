from django.db import models
from accounts.models import AuthUserModel
from students.models import StudentModel
from teachers.models import TeacherModel

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



class CourseEnrollmentModel(models.Model):
    student = models.ForeignKey(
        StudentModel,
        on_delete=models.CASCADE,
        related_name="student_enroll",
    )

    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
    )
    adminssion_fee = models.FloatField(null=True)
    pay = models.FloatField(null=True)
    due = models.FloatField(null=True)

    #A student cannot register for the same course a second time.
    # That's why use UniqueConstraint
    class Meta: 
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course" ],
                name="unique_student_course"
            )
        ]


    def __str__(self):
        return f"{self.student.name}"


    def save(self, *args, **kwargs):
        self.adminssion_fee = self.course.course_fee
        self.due = self.adminssion_fee - self.pay
        super().save(*args, **kwargs)




class TeacherAssignModel(models.Model):
    teacher = models.ForeignKey(
        TeacherModel, 
        on_delete=models.SET_NULL,
        related_name="course_teacher",
        null=True
    )
    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"{self.teacher.name} -- {self.course.title}"