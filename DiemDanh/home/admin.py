from django.contrib import admin
from .models import students,teachers,principals,history_attendance,UserProfile
# Register your models here.
admin.site.register(students)
admin.site.register(teachers)
admin.site.register(principals)
admin.site.register(history_attendance)
admin.site.register(UserProfile)