from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Donors
from app.models import Eligibility
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import auth
import random
from django.core.mail import send_mail
from django.contrib import messages

def Home(request):
    return render(request, 'home.html')


def Donor_home(request):
    return render(request, 'donor_login.html')

def Donor_register(request):
     return render(request, 'donor_register.html')


def Donor_form(request):
    if request.method == 'POST':
        b1 = request.POST['fname']
        b2 = request.POST['lname']
        b3 = request.POST['dob']
        b4 = request.POST['age']
        b5 = request.POST['gender']
        b6 = request.POST['mob']
        b7= request.POST['blood']  
        b8 = request.POST['address']  
        b9 = request.POST['district']  
        c = request.POST['email']  
        d = request.POST['username']  
        e = request.POST['password']  

        
        if User.objects.filter(username=d).exists():
            return HttpResponse("Username already exists. Please choose a different one.")
        
        d1 = User.objects.create_user(username=d, email=c, password=e)
        d1.save()
        
        
        d2 = Donors.objects.create(userid=d1, fname=b1, lname=b2, dob=b3, age=b4,  gender=b5, mob=b6, bloodgroup=b7 ,   address=b8 , district=b9)
        d2.save()
        
        return redirect(Donor_home)

    else:
        return render(request, 'donor_register.html')



def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            x=User.objects.get(id=request.user.id)
            y=Donors.objects.get(userid=x)
            return render(request, 'donor_home.html',{'donor_data':y})

        else:
            return render(request, 'donor_login.html',{'error':'Invalid username or password'})
        
    return render(request,'donor_login.html')

def Logout(request):
    auth.logout(request)
    return redirect(Login)

def donormain(request):
    if request.method == 'POST':
        previous_date= request.POST['previous_date']
        certificate = request.POST['certificate']

        # data = Donors.objects.create(donateddate = previous_date)
        # data.save()
        return render(request,'eligibility.html')
    else:
        return render(request,'donor_login.html')
    
# def Eligibilitys(request):
#     if request.method == 'POST':
#         q1= request.POST['q1']
#         q2 = request.POST['q2']
#         q3 = request.POST['q3']
#         q4 = request.POST['q4']
#         q5 = request.POST['q5']
#         q6 = request.POST['q6']
#         q7 = request.POST['q7']
#         q8 = request.POST['q8']
#         q9 = request.POST['q9']
#         q10 = request.POST['q10']
#         q11 = request.POST['q11']
#         q12 = request.POST['q12']
#         q13 = request.POST['q13']
#         q14 = request.POST['q14']
#         q15 = request.POST['q15']
#         q16 = request.POST['q16']
#         q17 = request.POST['q17']
#         q18 = request.POST['q18']
#         q19 = request.POST['q19']
#         q20 = request.POST['q20']

       
#         data = Eligibility.objects.create(questions=q1)
#         data.save()
    
#         return render(request, "donor_home.html")
#     else:
#         return render(request, 'eligibility.html')
#         # return HttpResponse('welcome')


def Eligibilitys(request):
    if request.method == "POST":
        # Loop through q1...q20
        for i in range(1, 21):
            q = request.POST.get(f'q{i}')      # question text
            a = request.POST.get(f'a{i}')      # answer (yes/no)

            # if q:  # only save non-empty
            #     Eligibility.objects.create(
            #         questions=q,
            #         answers=True if a == "yes" else False
            #     )

        return render(request, "eligibility.html") # redirect instead of rendering directly
    else:

        return render(request, "eligibility.html")


def qa_list(request):
    qas = Eligibility.objects.all()
    return render(request, 'qes.html', {"qas": qas})

    


def donor_profile(request):
    x=User.objects.get(id=request.user.id)
    y=Donors.objects.get(userid=x)
    return render(request,'donor_profile.html',{'data':y})

def donor_edit(request):
    x=User.objects.get(id=request.user.id)
    y=Donors.objects.get(userid=x)

    if request.method=='POST':
        y.fname = request.POST['fname']
        y.lname = request.POST['lname']
        y.dob = request.POST['dob']
        y.age = request.POST['age']
        y.gender = request.POST['gender']
        y.mob = request.POST['mob']
        y.bloodgroup= request.POST['blood']  
        y.address = request.POST['address']  
        y.district = request.POST['district']  
        y.userid.email = request.POST['email']  
        y.userid.username = request.POST['username']  
        y.save()
        y.userid.save()
        return redirect(donor_profile)
    
   

    else:
        return render(request,'donor_edit.html',{'data':y})
    


def donor_delete(request,id):
        data=Donors.objects.get( id=id)
        data.delete()
        return redirect(Logout)
    


def Recipient_home(request):

    return HttpResponse("hi")


def Recipient_serach(request):
    m = Donors.objects.all()
    return render(request, 'recipient.html', {'donor_data': m})




def send_otp(email):
    otp = random.randint(100000,999999)
    send_mail(
        'Your OTP Code',''
        f'Your OTP code is: {otp}',
        'jerisonjoseph.c007@gmail.com',
        [email],
        fail_silently=False,
    )
    return otp

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            otp = send_otp(email)

            context = {
                        "email": email,
                        "otp": otp,
            }
            return render(request,'verify_otp.html',context)
        
        except User.DoesNotExist:
            messages.error(request,'Email address not found.')
    else:
        return render(request,'password_reset.html')
    return render(request,'password_reset.html') 

def verify_otp(request):
    if request.method == 'POST':
        email =request.POST.get('email')
        otpold = request.POST.get('otpold')
        otp = request.POST.get('otp')

        if otpold==otp :
            context = {
                'otp' : otp,
                'email': email
            }
            return render(request,'set_new_password.html',context)
        else:
            messages.error(request,"Invalid OTP")
    return render(request,'verify_otp.html') 

def set_new_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password==confirm_password:
            try:
               
                user=User.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                messages.success(request,'Password has been reset successfully')
                return redirect(Login)
            except User.DoesNotExist:
                messages.error(request,'Password doesnot match')
        return render(request,'set_new_password.html',{'email':email})               
    return render(request,'set_new_password.html',{'email':email})

