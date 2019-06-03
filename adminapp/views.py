from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
import smtplib
from adminapp.models import *

# Create your views here.

def index(request):
    id=request.session['adminid']
    return render(request,"adminapp/index.html",{})

def view_user(request):
    data=tbl_reg.objects.all()
    return render(request,"adminapp/view_user.html",{'data':data})

def approve(request,id):
    aprv=tbl_reg.objects.get(id=id)
    if aprv.approve=="APPROVE":
        password = User.objects.make_random_password(length=5, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889") # zvk0hawf8m6394
        new=tbl_log.objects.create(username=aprv.email,password=password,usertype=aprv.usertype)
        mail=smtplib.SMTP('smtp.mailgun.org',587)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        message= "Hello, this message is from 'In Sum'.Your username is " + new.username + " and password is " + new.password + ". Thank you."
        email=aprv.email
        mail.sendmail(settings.EMAIL_HOST_USER,email,message)
        aprv.approve="APPROVED!!!"
        aprv.save()
    return HttpResponseRedirect(reverse('view_user'))

def view_auser(request):
    log=tbl_log.objects.all()
    return render(request,"adminapp/view_auser.html",{'log':log})

def delete(request,id):
    dele=tbl_log.objects.filter(id=id).delete()
    data=tbl_log.objects.all()
    return HttpResponseRedirect(reverse('view_auser'))

def view_search(request):
    txt=tbl_text.objects.all()
    return render(request,"adminapp/view_search.html",{'txt':txt})

def view_contact(request):
    msg=tbl_contact.objects.all()
    return render(request,"adminapp/view_contact.html",{'msg':msg})

