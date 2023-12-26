from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate
from .forms import*
from django.contrib import messages
# Create your views here.

def login(request):
    # check if the request is using form
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            try:
                username = request.POST['username']
                password = request.POST['password']
                
                #check if the credentials are correct
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    #redirect to home page
                    pass
                else: messages.error(request,"Error: Invalid username or password") #session of message
                return redirect("accountapp:login_url") #back to login
            except Exception as e:
                messages.error(request,f"Error: {e}")
            
    else:
        login_form = LoginForm() #provide the forms.py
    
    template = "login.html"
    context = {
        "form": login_form
    }
    return render(request,template,context)