from django.shortcuts import render,redirect,get_object_or_404
import random
from django.contrib.auth.models import User,auth
from django.contrib.auth import login as auth_login,authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Candidate,OTP,Placements,Volunteer
from django.contrib.auth.decorators import login_required


def generate_otp():
    return str(random.randint(100000,999999))

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        print(username)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            print('successful login')
            auth.login(request,user)
            messages.success(request,"Login Successfull")
            return redirect('/profile')
        else:
            print('Invalid Data')
            messages.info(request,"Invalid credentials")
            return redirect('/')
    return render(request,'student_login.html')


'''def c_register(request):
    if request.method=='POST':
        c_Name=request.POST['c_Name']
        c_Address=request.POST['c_Address']
        c_DOB=request.POST['c_DOB']
        c_Aadhaar=request.POST['c_Aadhaar']
        c_Email=request.POST['c_Email']
        c_Phone=request.POST['c_Phone']
        c_Institution=request.POST['c_Institution']
        c_Stream=request.POST['c_Stream']
        c_RegNo=request.POST['c_RegNo']
        c_CGPA=request.POST['c_CGPA']
        c_Semester=request.POST['c_Semester']
        c_PassoutYear=request.POST['c_PassoutYear']
        c_Photo=request.POST['c_Photo']
        c_Resume=request.POST['c_Resume']
        c_Marklist=request.POST['c_Marklist']
        password=request.POST['password']
        password1=request.POST['password1']
        c_SecQues=request.POST['c_SecQues']
        c_Ans=request.POST['c_Ans']
        if password!=password1:
            messages.info(request,"Password do not match.")
            return redirect('/c_register')
        if User.objects.filter(username=c_Email).exists():
            messages.info(request,"User already exists.")
            return redirect('/c_register')

        user=User.objects.create_user(username=c_Email,email=c_Email,password=password1)
        user.is_active=False
        user.save()
        Candidate.objects.create(user=user,c_Name=c_Name,c_Address=c_Address,c_DOB=c_DOB,c_Aadhaar=c_Aadhaar,c_Phone=c_Phone,c_Institution=c_Institution,c_Stream=c_Stream,c_RegNo=c_RegNo,c_CGPA=c_CGPA,c_Semester=c_Semester,c_PassoutYear=c_PassoutYear,c_Photo=c_Photo,c_Resume=c_Resume,c_Marklist=c_Marklist,c_SecQues=c_SecQues,c_Ans=c_Ans)


        otp_code=generate_otp()
        OTP.objects.create(user=user,otp=otp_code)


        mail_subject='Verify your email'
        message=f'Your OTP is {otp_code}.'
        send_mail(mail_subject,message,settings.DEFAULT_FROM_EMAIL,[c_Email])

        messages.success(request,'Please verify the OTP sent to your email.')
        return redirect('/verify_otp')
    
    return render(request,'student_register.html')'''
def register(request):
    if request.method=='POST':
        c_Name=request.POST['c_Name']
        c_Address=request.POST['c_Address']
        c_DOB=request.POST['c_DOB']
        c_Aadhaar=request.POST['c_Aadhaar']
        c_Email=request.POST['c_Email']
        c_Phone=request.POST['c_Phone']
        c_Institution=request.POST['c_Institution']
        c_Stream=request.POST['c_Stream']
        c_RegNo=request.POST['c_RegNo']
        c_CGPA=request.POST['c_CGPA']
        c_Semester=request.POST['c_Semester']
        c_PassoutYear=request.POST['c_PassoutYear']
        c_Photo=request.FILES['c_Photo']
        c_Resume=request.FILES['c_Resume']
        c_Marklist=request.FILES['c_Marklist']
        password=request.POST['password']
        password1=request.POST['password1']
        c_SecQues=request.POST['c_SecQues']
        c_Ans=request.POST['c_Ans']
        if password==password1:
            if User.objects.filter(username=c_Email).exists():
                messages.info(request,"User already exists.")
                return redirect('/register')
            else:
                user=User.objects.create_user(username=c_Email,email=c_Email,password=password1)
                user.is_active=False
                user.save()
                Candidate.objects.create(user=user,c_Name=c_Name,c_Address=c_Address,c_DOB=c_DOB,c_Aadhaar=c_Aadhaar,c_Phone=c_Phone,c_Institution=c_Institution,c_Stream=c_Stream,c_RegNo=c_RegNo,c_CGPA=c_CGPA,c_Semester=c_Semester,c_PassoutYear=c_PassoutYear,c_Photo=c_Photo,c_Resume=c_Resume,c_Marklist=c_Marklist,c_SecQues=c_SecQues,c_Ans=c_Ans)

                otp_code=generate_otp()
                OTP.objects.update_or_create(user=user,defaults={'otp':otp_code})

                mail_subject='Verify your email'
                message=f'Your OTP is {otp_code}.'
                send_mail(mail_subject,message,settings.DEFAULT_FROM_EMAIL,[c_Email])

                messages.success(request,'Please verify the OTP sent to your email.')
                return redirect('/verify_otp') 
        else:
            messages.info(request,"Password do not match.")
            return redirect('/register')
    return render(request,'student_register.html')



def verify_otp(request):
    if request.method=='POST':
        otp_code=request.POST['otp']
        try:
            otp=OTP.objects.get(otp=otp_code)
            user=otp.user
            user.is_active=True
            user.save()
            otp.delete()
            auth_login(request, user)
            messages.success(request,'Your account has been activated successfully')
            return redirect('/')
        except OTP.DoesNotExist:
            messages.info(request,'Invalid OTP')
            return redirect('/verify_otp')
    return render(request,'verify_otp.html')

@login_required
def profile(request):
    user=request.user
    candidate=user.candidate
    context={
        'user':user,
        'candidate':candidate
    }
    return render(request,'profile.html',context)

def joblisting(request):
    dict_placement={
        'pla':Placements.objects.all()
    }
    return render(request,'joblisting.html',dict_placement)

def about(request):
    return render(request,'about.html')

def privacy(request):
    return render(request,'privacy.html')

def support(request):
    dict_support={
        'vol':Volunteer.objects.all()
    }
    return render(request,'support.html',dict_support)

def terms(request):
    return render(request,'terms.html')

def update(request):
    return render(request,'update.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def company(request,company_id):
    comp=get_object_or_404(Placements,pk=company_id)
    return render(request,'company.html',{'comp':comp})