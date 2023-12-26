from django import forms
from .models import User
class LoginForm(forms.Form):
    username = forms.CharField(
        label="Email address/username",
        max_length=150,
        widget=forms.TextInput(attrs={
            "placeholder": 'Enter your email/username here...',
            "class": 'w-full rounded-md border border-border py-3 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary',
        })
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": 'Enter your password here...',
            "class": 'w-full rounded-md border border-border py-3 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary',
        })
    )

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="First name",
        max_length=80,
        widget=forms.TextInput(attrs={
            'placeholder':'Enter first name',
            'class':'w-full rounded-md border border-border py-3 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary',
        })
    )
    last_name = forms.CharField(
        label="Last name",
        max_length=80,
        widget=forms.TextInput(attrs={
            'placeholder':'Enter last name',
            'class':'w-full rounded-md border border-border py-3 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary',
        })
    )
    
    username = forms.CharField(
        label="Email address",
        widget=forms.TextInput(attrs={
            'placeholder':'Enter email address',
            'class':'w-full rounded-md border border-border py-3 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary',
        })
    )
    
    email = forms.EmailField(
        label="Email address",
        widget=forms.TextInput(attrs={
            'placeholder':'Enter email address',
            'class':'w-full rounded-md border border-border py-3 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary',
        })
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'placeholder':'Enter password',
            'class':'w-full rounded-md border border-border py-3 focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary',
            'autocomplete':'off'
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        username = cleaned_data.get("username")
        email = cleaned_data.get('email')
        password = cleaned_data.get("password")
        
        #check if username is already taken
        if User.objects.filter(username=username).exists():
            self.add_error('username','Username already taken')
            
        #check if email is already taken
        if User.objects.filter(email=email).exists():
            self.add_error("email","Email already taken")
        
        return cleaned_data
        
    