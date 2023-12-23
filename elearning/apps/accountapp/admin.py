from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import*

#admin site diplay
class CustomUser(UserAdmin):
    model = User
    list_display = ('username','email','first_name','last_name','is_instructor','is_staff')
    fieldsets = [
        (
            None,
            {
                "fields":['username','email','first_name','last_name','is_instructor','is_staff']
            }
        )
    ]
    
admin.site.register(User, CustomUser)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ['user','instructor_description','profile_img']
    
admin.site.register(Instructor,InstructorAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['instructor','title','date_created']
    
admin.site.register(Course, CourseAdmin)