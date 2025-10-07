from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app.models import Donors,CustomUser
from app.models import Recipient,Notification
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


# def Donor_form(request):
#     if request.method == 'POST':
#         b1 = request.POST['fname']
#         b2 = request.POST['lname']
#         b3 = request.POST['dob']
#         b4 = request.POST['age']
#         b5 = request.POST['gender']
#         b6 = request.POST['mob']
#         b7= request.POST['blood']  
#         b8 = request.POST['address']  
#         b9 = request.POST['district']  
#         c = request.POST['email']  
#         d = request.POST['username']  
#         e = request.POST['password']  

        
#         if User.objects.filter(username=d).exists():
#             return HttpResponse("Username already exists. Please choose a different one.")
        
#         d1 = User.objects.create_user(username=d, email=c, password=e)
#         d1.save()
        
        
#         d2 = Donors.objects.create(userid=d1, fname=b1, lname=b2, dob=b3, age=b4,  gender=b5, mob=b6, bloodgroup=b7 ,   address=b8 , district=b9)
#         d2.save()
        
#         return redirect(Donor_home)

#     else:
#         return render(request, 'donor_register.html')

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import CustomUser, Donors, Recipient  # make sure to import your models

# def register_user(request):
#     if request.method == 'POST':
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         mob = request.POST.get('mob')
#         blood = request.POST.get('blood')
#         address = request.POST.get('address')
#         district = request.POST.get('district')
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         role = request.POST.get('role')  # NEW: get role from form


#         # Check required fields
#         if not username or not email or not password or not role:
#          return HttpResponse("Please fill all required fields.")

#         # Check if username exists
#         if CustomUser.objects.filter(username=username).exists():
#             return HttpResponse("Username already exists. Please choose a different one.")



#         # Create the user with role
#         user = CustomUser.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#             first_name=fname,
#             last_name=lname,
#             role=role
#         )
#         user.save()

#         # Save additional info in Donors or Recipient table
#         if role == 'donor':
#             Donors.objects.create(
#                 userid=user,
#                 fname=fname,
#                 lname=lname,
#                 dob=dob,
#                 age=age,
#                 gender=gender,
#                 mob=mob,
#                 bloodgroup=blood,
#                 address=address,
#                 district=district
#             )
#             return redirect('Donor_home')  # adjust your URL name
#         elif role == 'recipient':
#             Recipient.objects.create(
#                 userid=user,
#                 fname=fname,
#                 lname=lname,
#                 dob=dob,
#                 age=age,
#                 gender=gender,
#                 mob=mob,
#                 bloodgroup=blood,
#                 address=address,
#                 district=district
#             )
#             return redirect('Recipient_login')  # adjust your URL name
#         else:
#             return HttpResponse("Invalid role selected.")

#     else:
#         return render(request, 'register.html')


def Register_user(request):
    if request.method == 'POST':
        # Get form data safely
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

        # Validate required fields
        if not username or not email or not password or not role:
            return HttpResponse("Please fill all required fields.")

        # Check if username already exists
        if CustomUser.objects.filter(username=username).exists():
            return HttpResponse("Username already exists. Please choose a different one.")

        # Create the user with role
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
            role=role
        )

        # Save additional info in Donors or Recipient table
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
            return redirect(Donor_home)  # Adjust URL name

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
            return redirect(Recipient_login)  # Adjust URL name

        else:
            return HttpResponse("Invalid role selected.")

    else:
        return render(request, 'register.html')  # Your registration template



# def Login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']

#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request, user)
#             x=User.objects.get(id=request.user.id)
#             y=Donors.objects.get(userid=x)
#             return render(request, 'donor_home.html',{'donor_data':y})

#         else:
#             return render(request, 'donor_login.html',{'error':'Invalid username or password'})
        
#     return render(request,'donor_login.html')

# def Login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)  
#             try:
#                 donor_data = Donors.objects.get(userid=user)
#                 return render(request, 'donor_home.html', {'donor_data': donor_data})
#             except Donors.DoesNotExist:
#                 try:
#                     recipient_data = Recipient.objects.get(userid=user)
#                     return render(request, 'recipient_home.html', {'recipient_data': recipient_data})
#                 except Recipient.DoesNotExist:
#                     return render(request, 'home.html', {'error': 'No profile found for this user.'})
#         else:
#             return render(request, 'home.html', {'error': 'Invalid username or password'})
#     return render(request, 'home.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # log the user in

            # Check role from CustomUser
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
                return redirect('/admin/')  # or your admin dashboard

            else:
                return render(request, 'home.html', {'error': 'Invalid role for this user.'})

        else:
            # return render(request, 'home.html', {'error': 'Invalid username or password'})
            return redirect(Home)

    return render(request, 'home.html')

def Logout(request):
    auth.logout(request)
    return redirect(Home)

def donormain(request):
    if request.method == 'POST':
        previous_date= request.POST['previous_date']
        # certificate = request.POST['certificate']
        certificate = request.FILES.get('certificate')  
        donor = Donors.objects.get(userid=request.user) 
        donor.certificate = certificate
        donor. donateddate = previous_date
        donor.save()
        return render(request,'eligibility.html')
    else:
        return render(request,'donor_home.html')
    

from django.shortcuts import render, redirect, get_object_or_404
from .models import Donors, Eligibility

# def Eligibilitys(request, userid):
#     donor = get_object_or_404(Donors, id=userid)
    
#     if request.method == "POST":
#         # Get form data
#         ans1 = request.POST.get('q1', 'Nill')
#         ans2 = request.POST.get('q2', 'Nill')
#         ans3 = request.POST.get('q3', 'Nill')
#         ans4 = request.POST.get('q4', 'Nill')
#         ans5 = request.POST.get('q5', 'Nill')
#         ans6 = request.POST.get('q6', 'Nill')
#         ans7 = request.POST.get('q7', 'Nill')
#         ans8 = request.POST.get('q8', 'Nill')
#         ans9 = request.POST.get('q9', 'Nill')
#         ans10 = request.POST.get('q10', 'Nill')
#         ans11 = request.POST.get('q11', 'Nill')
#         ans12 = request.POST.get('q12', 'Nill')
#         ans13 = request.POST.get('q13', 'Nill')
#         ans14 = request.POST.get('q14', 'Nill')
#         ans15 = request.POST.get('q15', 'Nill')
#         ans16 = request.POST.get('q16', 'Nill')
#         ans17 = request.POST.get('q17', 'Nill')
#         ans18 = request.POST.get('q18', 'Nill')
#         ans19 = request.POST.get('q19', 'Nill')
#         ans20 = request.POST.get('q20', 'Nill')

#         Eligibility.objects.create(
#             userid=donor,
#             ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, ans5=ans5,
#             ans6=ans6, ans7=ans7, ans8=ans8, ans9=ans9, ans10=ans10,
#             ans11=ans11, ans12=ans12, ans13=ans13, ans14=ans14, ans15=ans15,
#             ans16=ans16, ans17=ans17, ans18=ans18, ans19=ans19, ans20=ans20
#         )

#         return render(request, "donor_home.html") 

#     return render(request, 'eligibility_form.html', {'user': donor})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Eligibility

def Eligibilitys(request, userid):
    # user = get_object_or_404(User, id=userid)
    # donor_instance = Donors.objects.get(fname=request.user.first_name) 
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

        # ... add all questions similarly
        eligibility.save()
        return render(request, 'donor_home.html')  # or back to the same page

    return render(request, 'eligibility.html', {'eligibility_data': eligibility})





def view(request):
    # m = Eligibility.objects.all()
    # donor = Donors.objects.get(userid=request.user)
    # m = Eligibility.objects.get(userid=donor) 
     # Get the logged-in user (CustomUser)
    user = request.user
    
    # Get the eligibility instance for this user
    m = Eligibility.objects.get(userid=user)
    return render(request, 'qes.html', {'eligibility_data': m})



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
    


def donor_delete(request,id):
        data=Donors.objects.get( id=id)
        data.delete()
        return redirect('Logout')
    


def Recipient_login(request):

    return render(request, 'login.html')


def Recipient_home0(request):

    return render(request, 'recipient_home.html')

# def Recipient_home(request):
#     donors = Donors.objects.all()  # fetch all donors from DB
#     return render(request, 'recipient_home.html', {'donors': donors})

def Recipient_home(request, send_data=None):
    donors = Donors.objects.all()
    # If no notifications, send_data is empty list
    if send_data is None:
        send_data = []
    return render(request, 'recipient_home.html', {'donors': donors, 'send_data': send_data})




def Recipient_serach(request):
    m = Donors.objects.all()
    return render(request, 'recipientsearch.html', {'donor_data': m})


def Recipient_register(request):
     return render(request, 'recipient_register.html')


# def Recipient_form(request):
#     if request.method == 'POST':
#         b1 = request.POST['fname']
#         b2 = request.POST['lname']
#         b3 = request.POST['dob']
#         b4 = request.POST['age']
#         b5 = request.POST['gender']
#         b6 = request.POST['mob']
#         b7= request.POST['blood']  
#         b8 = request.POST['address']  
#         b9 = request.POST['district']  
#         c = request.POST['email']  
#         d = request.POST['username']  
#         e = request.POST['password']  

        
#         if User.objects.filter(username=d).exists():
#             return HttpResponse("Username already exists. Please choose a different one.")
        
#         d1 = User.objects.create_user(username=d, email=c, password=e)
#         d1.save()
        
        
#         d2 = Recipient.objects.create(userid=d1, fname=b1, lname=b2, dob=b3, age=b4,  gender=b5, mob=b6, bloodgroup=b7 ,   address=b8 , district=b9)
#         d2.save()
        
#         return redirect(Recipient_login)

#     else:
#         return render(request, 'recipient_register.html')
    


def Recipient_profile(request):
    x=CustomUser.objects.get(id=request.user.id)
    y=Recipient.objects.get(userid=x)
    return render(request,'recipient_profile.html',{'data':y})


# def filter_donors(request):
#     if request.method == 'POST':
#         bloodgroup = request.POST.get('blood')
#         district = request.POST.get('district')

#         donor = Donors.objects.all()

#     if bloodgroup:
#         donor = donor.filter(bloodgroup__iexact=bloodgroup)
#     if district:
#         donor= donor.filter(district__iexact=district)

#     print(bloodgroup)
#     print(district)

#     donor_list = list(donor.values('fname', 'bloodgroup', 'district', 'age', 'mob'))

#     if donor_list:  
#         return render(request, 'recipientsearch.html', {'filter_data': donor_list})
#     else: 
#         return redirect('Recipient_home0')


def filter_donors(request):
    donor = Donors.objects.all()  # always start with all donors

    bloodgroup = None
    district = None

    if request.method == 'POST':
        bloodgroup = request.POST.get('blood')
        district = request.POST.get('district')

        if bloodgroup:
            donor = donor.filter(bloodgroup__iexact=bloodgroup)
        if district:
            donor = donor.filter(district__iexact=district)

    donor_list = list(donor.values('id', 'fname', 'bloodgroup', 'district', 'age', 'mob','gender' ,'address','donateddate','certificate'))

    if donor_list:
        return render(request, 'recipientsearch.html', {'filter_data': donor_list})
    else:
        return render(request, 'recipient_home.html')


    
    
# def notify_donor(request):
#     if request.method == 'POST':
#         donor_id = request.POST.get('select')
#         donor = get_object_or_404(Donors, id=donor_id)
#         recipient = request.user
#         Notification.objects.create(
#             donor=donor.user,  
#             recipient=recipient,
#             message=f"{recipient.username} has selected you for blood donation."
#         )

#         messages.success(request, "Donor has been notified!")
#         return redirect('Recipient_home')
#     else:
#         return redirect('Recipient_home')
    


# def donor_notifications(request):
#     notifications = Notification.objects.filter(donor=request.user, seen=False)
#     return render(request, 'donor_notifications.html', {'notifications': notifications})

# def send_donor(request):
#     if request.method == "POST":
#         donor_id = request.POST.get("select")
#         donor = Donors.objects.get(id=donor_id)
#         # Do whatever you want with donor_id
#         print("Selected Donor:", donor.fname)
#         # Redirect or render response
#         return redirect('recipient_home')



def send_donor(request):
    if request.method == "POST":
        donor_id = request.POST.get("select")
        
        # Safety check: make sure donor_id exists
        if not donor_id:
            print("No donor ID received!")
            return redirect('recipient_home')
        
        # Safely get the donor object
        donor = get_object_or_404(Donors, id=donor_id)
        print("Selected Donor:", donor.fname)
        
        # You can add further processing here
        # For example, mark as sent, send details, etc.
        donors = Donors.objects.all()
        return render(request, 'recipient_home.html',{
            'donors': donors,
            'send_data': [donor]  # wrap in list for template loop
        })
    
    
    # Optional: redirect if someone tries to GET this URL directly
    return redirect('recipient_home')







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

