from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, get_user_model
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

User = get_user_model()

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                #get data from the form
                username = form.cleaned_data.get('username')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                #add new user
                new_user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    is_instructor=False  # You can set this based on your logic
                )
                new_user.save()
                messages.success(request,message="New account created")
                return redirect('accountapp:login_url') #login page
            except Exception as e:
                messages.error(request,message=f"Error: {e}")
    else:
        form = RegistrationForm()

    template = "registration.html"
    context = {
        "form": form,
    }

    return render(request, template, context)
