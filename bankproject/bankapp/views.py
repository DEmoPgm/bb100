from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username  is already taken")
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('/login')



        else:
            messages.info(request,"Password is not matching")


    return render(request,"register.html")


def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=username,password=pswd)

        if user is not None:
            auth.login(request,user)
            return redirect('/newpage')
        else:
            messages.info(request,"Invalid Credentials")
            return  redirect('/login')

    return render(request,"login.html")

def form(request):
    return render(request,"form.html")


def newpage(request):
    return render(request,"newpage.html")


def logout(request):
    auth.logout(request)
    return redirect('/login')