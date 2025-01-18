from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

#Database hs
class student(models.Model):
    name = models.CharField(max_length=255)
    gender = models.BooleanField()
    birth_day = models.DateField(null=True, blank=True)
    id = models.IntegerField(_("Student ID"), primary_key=True)
    email = models.EmailField(_("Email Address"), unique=True)
    

    #Database gv
class teacher(models.Model):
    name_teacher = models.CharField(max_length=255, null=True)
    gender = models.BooleanField()
    birth_day = models.DateField(null=True, blank=True)
    id = models.IntegerField(_("Teacher ID"), primary_key=True)
    email = models.EmailField(_("Email Address"), unique=True)


class principal(models.Model):
    name_principal = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=255, default="Default Role")
    gender = models.BooleanField()
    birth_day = models.DateField(null=True, blank=True)
    id = models.IntegerField(_("Principal ID"), primary_key=True)
    email = models.EmailField(_("Email Address"), unique=True)
