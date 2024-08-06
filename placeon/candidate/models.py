from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Candidate(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    c_Name=models.CharField(max_length=100,blank=True)
    c_Address=models.CharField(max_length=200,blank=True)
    c_DOB=models.DateField(null=True,blank=True)
    c_Aadhaar=models.CharField(max_length=100,blank=True)
    c_Phone=models.CharField(max_length=100,blank=True)
    c_Institution=models.CharField(max_length=100,blank=True)
    c_Stream=models.CharField(max_length=100,blank=True)
    c_RegNo=models.CharField(max_length=100,blank=True)
    c_CGPA=models.FloatField(null=True,blank=True)
    c_Semester=models.CharField(max_length=100,blank=True)
    c_PassoutYear=models.CharField(max_length=4,blank=True)
    c_Photo=models.ImageField(upload_to='profiles/')
    c_Resume=models.FileField(upload_to='resumes/')
    c_Marklist=models.FileField(upload_to='marklists/')
    c_SecQues=models.CharField(max_length=100,blank=True)
    c_Ans=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.username
    
class OTP(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.otp}'


class Placements(models.Model):
    img=models.ImageField(upload_to='pics/')
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=1000)
    link=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Volunteer(models.Model):
    v_name=models.CharField(max_length=100)
    v_dept=models.CharField(max_length=100)
    v_contact=models.CharField(max_length=10)
    def __str__(self):
        return self.v_name