from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from ..accountapp.models import User, Instructor
from ..courseapp.models import *
# Create your views here.
@login_required(login_url='/account/') #get back to login
def dashboard(request):
    
    is_instructor = request.user.is_instructor
    
    if not is_instructor:
        #redirect to login and decide whether it should be on homepage or should log in first
        return redirect('accountapp:login_url')
    else: 
        # go to dashboard page
        instructor = Instructor.objects.get(user=request.user)
        templates = "dashboard.html"
        courses = GetCourses(instructor)
        full_name = f"{request.user.first_name} {request.user.last_name}"
        context = {
            "courses":courses,
            "instructor":full_name,
        }

        return render(request,templates,context)
    
    
def GetCourses(instructor):
    course_obj = Course.objects.filter(instructor=instructor)

    course_data = []

    for course in course_obj:
        total_modules = Module.objects.filter(course=course).count()
        total_students = Enrollment.objects.filter(course=course).count()
        print(total_modules)
        course_info = {
            "Title": course.title,
            "Description": course.description,
            "Image": course.course_img,
            "Published_date": course.formatted_date(),
            "Module_count":total_modules,
            "Student_count":total_students,
        }
        course_data.append(course_info)

    return course_data
