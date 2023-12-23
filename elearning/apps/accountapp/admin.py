from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#admin site diplay
class CustomUser(UserAdmin):
    model = User
    list_display = ('username','email','first_name','last_name','is_instructor','is_staff')
    fieldsets = [
        (
            None,
            {
                "fields":['username','email','first_name','last_name','is_instructor','is_staff']
            }
        )
    ]
    
admin.site.register(User, CustomUser)