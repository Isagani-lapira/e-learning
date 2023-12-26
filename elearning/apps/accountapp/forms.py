from django import forms

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
