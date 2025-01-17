from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=255)
    gender = models.BooleanField()
    birth_day = models.DateField()
    id = models.IntegerField(_("Student ID"), primary_key=True)
    email = models.EmailField(_("Email Address"), unique=True)