from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# register user.
def register(request):
        if request.method=="POST":
            fn=request.POST.get('firstname')
            ln=request.POST.get('lastname')
            email1=request.POST.get('email')
            pwd=request.POST.get('password')
            cpwd=request.POST.get('confirm_password') 
            user_name=request.POST.get('username')
           
            if  pwd == cpwd :
                if User.objects.filter(email=email1).exists():
                     messages.error(request,"user email already exits")
                elif User.objects.filter(username=user_name).exists():
                     messages.error(request,"username already taken")     
                else:     
                    User.objects.create(first_name=fn,last_name=ln,email=email1,password=make_password(pwd),username=user_name)
                    messages.success(request,"Registration Successful")
                    return  redirect("dashboard")
            else:
                 messages.error(request,"password do not match")    
        return render(request,"register.html")

#login user
def signin (request):
      return render(request,"login.html")








#dashboard
def dashboard(request):
    return render(request,"dashboard.html")




#logout user
def signout(request):
    return render (request,"register.html")