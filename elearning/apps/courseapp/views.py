from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    return HttpResponse("Course apps")

def DeleteCourse(request, course_id):
    try:
        delete_course = Course.objects.filter(id=course_id).delete() #delete selected course
        
        if delete_course:
            messages.success(request,"Success: Course deleted")
        return redirect(request.META.get('HTTP_REFERER','/')) #go back to previous url
    except Exception as e:
        messages.error(request, f"Error: {e}")
        print(e)
        return redirect(request.META.get('HTTP_REFERER','/')) #go back to previous url

def CourseInfo(request):
    template = "course_info.html"
    return render(request, template)