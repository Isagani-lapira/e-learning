from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
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
        course_form = CourseForm()
        instructor = Instructor.objects.get(user=request.user)
        templates = "dashboard.html"
        courses = GetCourses(instructor)
        full_name = f"{request.user.first_name} {request.user.last_name}"
        context = {
            "courses":courses,
            "instructor":full_name,
            "forms":course_form,
        }

        return render(request,templates,context)
    
# ------------ Display courses -----------------   
def GetCourses(instructor):
    course_obj = Course.objects.filter(instructor=instructor)

    course_data = []

    for course in course_obj:
        course_info = {
            "ID":course.id,
            "Title": course.title,
            "Description": course.description,
            "Image": course.course_img,
            "Published_date": course.formatted_date(),
            "Module_count":course.count_modules,
            "Student_count":course.count_enrolled,
        }
        course_data.append(course_info)

    return course_data


# ------------ Create new course ---------------
login_required(login_url="/account/")
def AddCourse(request):
    if request.method == "POST":
        try:
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                
                 # add new course data
                instructor = Instructor.objects.get(user = request.user)
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                course_img = form.cleaned_data['course_img']
                certificate = form.cleaned_data['certificate']
                
                course_obj = Course(instructor = instructor,
                                title = title,
                                description=description, 
                                course_img = course_img,
                                certificate = certificate)

                course_obj.save()
                messages.success(request,"Success: New course added.")
            else:
                messages.error(request, f"Error: {form.errors}")
        except Exception as e:
            messages.error(request, f"Error: {e}")
            
    #back to previous page
    previous_page = request.META.get('HTTP_REFERER')
    return redirect(previous_page)




# ------------- edit course ---------------------
def EditCourse(request,id):
    templates = "editcourse.html"

    #starting data
    course_obj = Course.objects.get(id=id)
    context = {
        "course_obj":course_obj,
        "course_id":id,
        "title":course_obj.title,
    }
    
    return render(request, templates, context)