from django import forms


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
    