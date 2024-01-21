from django import forms
from ckeditor.widgets import CKEditorWidget

class CourseForm(forms.Form):
    title = forms.CharField(
        label="Course Title",
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder':'Enter course title',
            "class":'w-full border border-border rounded-md focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary mb-2'
        })
    )
    
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={
            'placeholder':'Provide more detail description about this course',
            "class":'w-full border border-border rounded-md resize-none h-64 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary mb-2',
        })
    )
    course_img = forms.ImageField(
        label="Course Logo",
        widget=forms.ClearableFileInput())
    
    certificate = forms.ImageField(
        label="Certificate (Image format)",
        widget=forms.ClearableFileInput())
    
    
class ModuleForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label="Module Title",
        widget=forms.TextInput(attrs={
            'placeholder':'Enter module title',
            'class':'w-full border border-border rounded-md focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary mb-2'
        })
    )
    
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={
            'placeholder':'Enter description for this module',
            'class':'w-full border border-border rounded-md resize-none h-64 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary mb-2'
        })
    )
    
    cover_img = forms.ImageField(
        widget=forms.ClearableFileInput(),
        required=False)
    
    
class LessonForm(forms.Form):
    
    module = forms.CharField(
        widget=forms.TextInput(attrs={
        'id':'module_id',
        'type':'hidden'
    })
    )
    title = forms.CharField(
        max_length=150,
        label="Lesson Title",
        widget=forms.TextInput(attrs={
            'placeholder':'Enter Lesson title',
            'class':'w-full border border-border rounded-md focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary mb-2'
        })
    )
    content = forms.CharField(widget=CKEditorWidget())
    cover_img = forms.ImageField(
        widget=forms.ClearableFileInput(),
        required=False
    )