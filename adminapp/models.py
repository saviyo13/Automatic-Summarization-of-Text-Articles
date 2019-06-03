from django.db import models

#username-insum & password-insum

# Create your models here.

class tbl_log(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

class tbl_reg(models.Model):
    name=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    approve=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

class tbl_text(models.Model):
    inputtype=models.CharField(max_length=50)
    inputtxt=models.CharField(max_length=10000000000000)
    outputtxt=models.CharField(max_length=10000000000000)
    audio=models.FileField(verbose_name='file',null=True,blank=True)

class tbl_contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=1000)
    message=models.CharField(max_length=10000)