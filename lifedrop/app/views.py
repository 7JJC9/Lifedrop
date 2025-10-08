from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Donors,CustomUser,Send
from app.models import Recipient
from app.models import Eligibility
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import auth
import random
from django.core.mail import send_mail
from django.contrib import messages


def Home(request):
    return render(request, 'home.html')

def Register_home(request):
    return render(request, 'register.html')


def Donor_home(request):
    return render(request, 'login.html')

def Donor_register(request):
     return render(request, 'donor_register.html')



def Register_user(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mob = request.POST.get('mob')
        blood = request.POST.get('blood')
        address = request.POST.get('address')
        district = request.POST.get('district')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

       
        if not username or not email or not password or not role:
            return HttpResponse("Please fill all required fields.")

       
        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different one.")

       
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
            role=role
        )

        
        if role == 'donor':
            Donors.objects.create(
                userid=user,
                fname=fname,
                lname=lname,
                dob=dob,
                age=age,
                gender=gender,
                mob=mob,
                bloodgroup=blood,
                address=address,
                district=district
            )
            return redirect(Donor_home)  

        elif role == 'recipient':
            Recipient.objects.create(
                userid=user,
                fname=fname,
                lname=lname,
                dob=dob,
                age=age,
                gender=gender,
                mob=mob,
                bloodgroup=blood,
                address=address,
                district=district
            )
            return redirect(Recipient_login)  

        else:
            return HttpResponse("Invalid role selected.")

    else:
        return render(request, 'register.html')  



def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 

          
            if user.role == 'donor':
                try:
                    donor_data = Donors.objects.get(userid=user)
                    return render(request, 'donor_home.html', {'donor_data': donor_data})
                except Donors.DoesNotExist:
                    return render(request, 'home.html', {'error': 'Donor profile not found.'})

            elif user.role == 'recipient':
                try:
                    recipient_data = Recipient.objects.get(userid=user)
                    return render(request, 'recipient_home.html', {'recipient_data': recipient_data})
                except Recipient.DoesNotExist:
                    return render(request, 'home.html', {'error': 'Recipient profile not found.'})

            elif user.role == 'admin':
                return redirect('/admin/')  

            else:
                return render(request, 'home.html', {'error': 'Invalid role for this user.'})

        else:
          
            return redirect(Home)

    return render(request, 'home.html')

def Logout(request):
    auth.logout(request)
    return redirect(Home)

def donormain(request):
    if request.method == 'POST':
        previous_date= request.POST['previous_date']
        certificate = request.FILES.get('certificate')  
        donor = Donors.objects.get(userid=request.user) 
        donor.certificate = certificate
        donor. donateddate = previous_date
        donor.save()
        return render(request,'eligibility.html')
    else:
        return render(request,'donor_home.html')
    


def Eligibilitys(request, userid):
   
    donor = Donors.objects.get(userid=request.user)
    eligibility, created = Eligibility.objects.get_or_create(userid=donor.userid)

    if request.method == "POST":

        eligibility.ans1 = request.POST.get('q1')
        eligibility.ans2 = request.POST.get('q2')
        eligibility.ans3 = request.POST.get('q3')
        eligibility.ans4 = request.POST.get('q4')
        eligibility.ans5 = request.POST.get('q5')
        eligibility.ans6 = request.POST.get('q6')
        eligibility.ans7 = request.POST.get('q7')
        eligibility.ans8 = request.POST.get('q8')
        eligibility.ans9 = request.POST.get('q9')
        eligibility.ans10 = request.POST.get('q10')
        eligibility.ans11 = request.POST.get('q11')
        eligibility.ans12 = request.POST.get('q12')
        eligibility.ans13 = request.POST.get('q13')
        eligibility.ans14 = request.POST.get('q14')
        eligibility.ans15 = request.POST.get('q15')
        eligibility.ans16 = request.POST.get('q16')
        eligibility.ans17 = request.POST.get('q17')
        eligibility.ans18 = request.POST.get('q18')
        eligibility.ans19 = request.POST.get('q19')
        eligibility.ans20 = request.POST.get('q20')

       
        eligibility.save()
        return render(request, 'donor_home.html')  

    return render(request, 'eligibility.html', {'eligibility_data': eligibility})



def view(request):

    user = request.user
    m = Eligibility.objects.get(userid=user)
    return render(request, 'qes.html', {'eligibility_data': m})


def click(request, donor_id):

    try:
        donor = Donors.objects.get(id=donor_id)
    except Donors.DoesNotExist:
        return render(request, 'qes.html', {'eligibility_data': None, 'error': 'Donor not found.'})

    eligibility_data = Eligibility.objects.filter(userid=donor.userid).first()

    return render(request, 'qes.html', {'eligibility_data': eligibility_data, 'donor': donor})




def qa_list(request):
    qas = Eligibility.objects.all()
    return render(request, 'qes.html', {"qas": qas})

    


def donor_profile(request):

    x=CustomUser.objects.get(id=request.user.id)
    y=Donors.objects.get(userid=x)
    return render(request,'donor_profile.html',{'data':y})

def donor_edit(request):

    x=CustomUser.objects.get(id=request.user.id)
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
    
    


def Recipient_login(request):

    return render(request, 'login.html')


def Recipient_home0(request):

    return render(request, 'recipient_home.html')


def Recipient_home(request, send_data=None):
    donors = Donors.objects.all()
    if send_data is None:
        send_data = []
    return render(request, 'recipient_home.html', {'donors': donors, 'send_data': send_data})


def Recipient_serach(request):
    m = Donors.objects.all()
    return render(request, 'recipientsearch.html', {'donor_data': m})


def Recipient_register(request):
     return render(request, 'recipient_register.html')



def Recipient_profile(request):
    x=CustomUser.objects.get(id=request.user.id)
    y=Recipient.objects.get(userid=x)
    return render(request,'recipient_profile.html',{'data':y})



def Recipient_edit(request):

    x=CustomUser.objects.get(id=request.user.id)
    y=Recipient.objects.get(userid=x)

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
        return redirect(Recipient_profile)

    else:
        return render(request,'recipient_edit.html',{'data':y})



def filter_donors(request):
    donor = Donors.objects.all()  

    bloodgroup = None
    district = None

    if request.method == 'POST':
        bloodgroup = request.POST.get('blood')
        district = request.POST.get('district')

        if bloodgroup:
            donor = donor.filter(bloodgroup__iexact=bloodgroup)
        if district:
            donor = donor.filter(district__iexact=district)

    if donor.exists():  
        return render(request, 'recipientsearch.html', {'filter_data': donor})
    else:
        return render(request, 'recipient_home.html')


def send_donor(request):
    if request.method == 'POST':
        donor_id = request.POST.get('select')  
        donor = Donors.objects.get(id=donor_id)
        donor_data = Donors.objects.all()

        
        Send.objects.create(
            recipient=request.user,
            donor=donor
        )

        
        sent_donors = Send.objects.filter(recipient=request.user)

        return render(request, 'donor_home.html', {
        'donor_data': donor_data,
        'sent_donors': sent_donors,
        'user': request.user
    })
        

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
            user = CustomUser.objects.get(email=email)
            otp = send_otp(email)

            context = {
                        "email": email,
                        "otp": otp,
            }
            return render(request,'verify_otp.html',context)
        
        except CustomUser.DoesNotExist:
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
               
                user=CustomUser.objects.get(email=email)
                user.set_password(new_password)
                user.save()
                messages.success(request,'Password has been reset successfully')
                return redirect(Login)
            except CustomUser.DoesNotExist:
                messages.error(request,'Password doesnot match')
        return render(request,'set_new_password.html',{'email':email})               
    return render(request,'set_new_password.html',{'email':email})

