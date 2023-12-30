from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['instructor','title','date_created']
    
admin.site.register(Course, CourseAdmin)