from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages

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
        print(e)
        return redirect(request.META.get('HTTP_REFERER','/')) #go back to previous url
    
    
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