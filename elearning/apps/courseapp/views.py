from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from ..instructorapp.forms import ModuleForm
from .models import *

def index(request):
    return HttpResponse("Course apps")


# ---------- delete course ------------
def DeleteCourse(request, course_id):
    try:
        delete_course = Course.objects.filter(id=course_id).delete() #delete selected course
        
        if delete_course:
            messages.success(request,"Success: Course deleted")
        return redirect(request.META.get('HTTP_REFERER','/')) #go back to previous url
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect(request.META.get('HTTP_REFERER','/')) #go back to previous url

def CourseInfo(request):
    template = "course_info.html"
    return render(request, template)
    
    
# -------------- add module --------------------
def AddModule(request, id):
    
    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            cover_img = form.cleaned_data['cover_img']
            course_obj = Course.objects.get(id=id) #course object


            try:
                new_data = None
                # no image added
                if cover_img is None:
                    new_data = Module(course=course_obj,
                                        title=title,
                                        description=description)
                else: #added with image included
                    new_data = Module(course=course_obj,
                                        title=title,
                                        description=description,
                                        cover_img = cover_img)
                new_data.save()
                    
                messages.success(request,"Success: New Module add.")
            except Exception as e:
                messages.error(request,f"Error: {e}")
        
    return redirect(request.META.get('HTTP_REFERER','/')) # go back to previous url




# ------------ Delete module ----------
login_required(login_url="/account/")
def deleteModule(request, id):
    if request.method == 'GET':
        try:
            module_obj = get_object_or_404(Module, id=id)
            module_name = module_obj.title
            module_obj.delete()
            messages.success(request,f"Module {module_name} successfully deleted.")
        except Exception as e:
            messages.error(request,f"Error: {e}")
            
            
    return redirect(request.META.get('HTTP_REFERER','/'))


# ------------ delete lesson -----------------
def deleteLesson(request,id):
    if request.method == 'GET':
        try:
            lesson_obj = get_object_or_404(Lesson,id=id)
            lesson_title = lesson_obj.title
            lesson_obj.delete()
            
            #return message with title included
            messages.success(request, f"Lesson {lesson_title} successfully deleted.")
        except Exception as e:
            messages.error(request,f"Error: {e}")

    return redirect(request.META.get('HTTP_REFERER','/')) #back to previous page
