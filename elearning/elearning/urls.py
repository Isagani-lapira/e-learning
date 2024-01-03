
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path
from apps.accountapp import urls as account_url
from apps.profileapp import urls as profile_url
from apps.courseapp import urls as course_url
from apps.instructorapp import urls as instructor_url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.static import serve 

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'base.html'), name='empty_url'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('account/', include(account_url)),
    path('profile/', include(profile_url)),
    path('course/', include(course_url)),
    path('instructor/', include(instructor_url))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
