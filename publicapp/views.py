from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,"publicapp/home.html",{})

def about(request):
    return render(request,"publicapp/about.html",{})

def service(request):
    return render(request,"publicapp/service.html",{})

def register(request):
    if request.method=="POST":
        na=request.POST.get('r1')
        lna=request.POST.get('r2')
        ge=request.POST.get('r3')
        dob=request.POST.get('r4')
        mail=request.POST.get('r5')
        des=request.POST.get('r6')
        data=tbl_reg.objects.create(name=na,lname=lna,gender=ge,dob=dob,email=mail,designation=des,usertype='user',approve='APPROVE')
        return render(request,"publicapp/success.html",{})
    return render(request,"publicapp/register.html",{})

def success(request):
    return render(request,"publicapp/success.html",{})

def login(request):
    if request.method=="POST":
        uname=request.POST.get('l1')
        psw=request.POST.get('l2')
        if tbl_log.objects.filter(username=uname,password=psw):
            data=tbl_log.objects.get(username=uname,password=psw)
            usertype=data.usertype
            if usertype=="admin":
                request.session["adminid"]=data.id
                return HttpResponseRedirect(reverse('index')) 
            if usertype=="user":
                data2=tbl_reg.objects.get(email=uname)
                request.session["userid"]=data2.id
                return HttpResponseRedirect(reverse('profile'))
        return render(request,"publicapp/error.html")
    return render(request,"publicapp/login.html",{})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('home'))

def contact(request):
    if request.method=="POST":
        na=request.POST.get('c1')
        mail=request.POST.get('c2')
        sub=request.POST.get('c3')
        msg=request.POST.get('c4')
        var=tbl_contact.objects.create(name=na,email=mail,subject=sub,message=msg)
        return render(request,"publicapp/csuccess.html",{})
    return render(request,"publicapp/contact.html",{})

def csuccess(request):
    return render(request,"publicapp/csuccess.html",{})

def error(request):
    return render(request,"publicapp/error.html",{})