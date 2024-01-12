from django.contrib import admin
from .models import *
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['instructor','title','date_created']
    
admin.site.register(Course, CourseAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student','course','date_enrolled','is_finish']
    
admin.site.register(Enrollment, EnrollmentAdmin)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id','course','title','description','cover_img']
    
admin.site.register(Module,ModuleAdmin)

class LessonAdmin(admin.ModelAdmin):
    list_display = ['module','title','content','cover_img']

admin.site.register(Lesson,LessonAdmin)