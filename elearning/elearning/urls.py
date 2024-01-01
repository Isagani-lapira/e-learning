from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from apps.accountapp import urls as account_url
from apps.profileapp import urls as profile_url
from apps.courseapp import urls as course_url
from apps.instructorapp import urls as instructor_url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'base.html'), name='empty_url'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('account/', include(account_url)),
    path('profile/', include(profile_url)),
    path('course/', include(course_url)),
    path('instructor/', include(instructor_url))
]
