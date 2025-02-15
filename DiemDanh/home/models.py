from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth.models import User



# Create your models here.

#Database hs
class students(models.Model):
    id = models.IntegerField(_("ID"), primary_key=True)
    name_student = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    birth_day = models.DateField(null=True, blank=True)
    email = models.EmailField(_("Email Address"), unique=True)
    contactPH = models.CharField(max_length=15, unique=True)

    #Database gv
class teachers(models.Model):
    id = models.IntegerField(_("ID"), primary_key=True)
    name_teacher = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    birth_day = models.DateField(null=True, blank=True)
    teacher_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_("Email Address"), unique=True)
    contact = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name_teacher


class principals(models.Model):
    id = models.IntegerField(_("Principal ID"), primary_key=True)
    name_principal = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=255, default="Default Role")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    birth_day = models.DateField(null=True, blank=True)
    email = models.EmailField(_("Email Address"), unique=True)

class history_attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused')  # Thêm trạng thái "Excused" (có phép)
    ]

    id = models.IntegerField(_("ID"), primary_key=True)
    student_name = models.CharField(max_length=255)  # Tên học viên
    student_id = models.CharField(max_length=50, unique=True)  # Mã số học viên
    class_name = models.CharField(max_length=100)  # Lớp học
    checkin_time = models.TimeField(null=True, blank=True)  # Giờ check-in
    date_attendance = models.DateField(default=now)  # Mặc định là ngày hiện tại
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present')  # Trạng thái điểm danh
    notes = models.TextField(null=True, blank=True)  # Ghi chú thêm nếu cần

    def __str__(self):
        return f"{self.student_name} ({self.student_id}) - {self.date_attendance} - {self.status}"

    class Meta:
        ordering = ['-date_attendance']  # Sắp xếp theo ngày điểm danh mới nhất


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)