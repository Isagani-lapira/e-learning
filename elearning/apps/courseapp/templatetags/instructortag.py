from django import template
from ..models import Module

register = template.Library()

@register.simple_tag
def RetrieveCourseModule(course):
    # get all the module title for a specific course
    module_title = Module.objects.filter(course=course).values_list('title', flat=True)
    
    return module_title
