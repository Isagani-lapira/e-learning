from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from ..accountapp.models import User
# Create your views here.
@login_required(login_url='/account/') #get back to login
def dashboard(request):
    
    is_instructor = request.user.is_instructor
    
    if not is_instructor:
        #redirect to login and decide whether it should be on homepage or should log in first
        print(is_instructor)
        return redirect('accountapp:login_url')
    else: 
        # go to dashboard page
        templates = "dashboard.html"
        context = {}
        return render(request,templates,context)