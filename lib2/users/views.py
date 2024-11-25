from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from users.models import CustomUser
from users.models import Users
# Create your views here.
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']

        user=authenticate(username=u,password=p)
        if user and user.is_superuser==True:
            login(request,user)
            return redirect('books:home')
        elif user and user.is_user==True:
            login(request, user)
            return redirect('books:home')

        else:
            return HttpResponse("invalid")

    return render(request,'login.html')

def admin_register(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp= request.POST['cp']
        f= request.POST['f']
        l= request.POST['l']
        e= request.POST['e']
        a= request.POST['address']
        phn= request.POST['phn']

        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,address=a,phone=phn,is_superuser=True)
            u.save()
        else:
            return HttpResponse("password is not same")
        return redirect('users:login')

    return render(request,'adminregister.html')



def user_register(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp= request.POST['cp']
        f= request.POST['f']
        l= request.POST['l']
        e= request.POST['e']
        a= request.POST['address']
        phn= request.POST['phn']

        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,address=a,phone=phn,is_user=True)
            u.save()
        else:
            return HttpResponse("password is not same")
        return redirect('users:login')

    return render(request,'userregister.html')



@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')

def view_users(request):
    k=Users.objects.all()
    return render(request,'viewuser.html',{'users':k})