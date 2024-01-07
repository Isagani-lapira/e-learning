from django import template
from ..models import Module, Lesson

register = template.Library()

@register.simple_tag
def RetrieveCourseModule(course):
    # get all the module title and object for a specific course
    modules = Module.objects.filter(course=course)
    module_dict = {module.title: module for module in modules}
    return module_dict

@register.simple_tag
def ModuleLesson(module):
    #retrieve all lessons for every courses
    lessons = Lesson.objects.filter(module=module ).values_list('title',flat=True)
    return lessons