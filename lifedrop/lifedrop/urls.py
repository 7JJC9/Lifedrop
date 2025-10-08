"""
URL configuration for lifedrop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),


# register

    path('',views.Home,name=''),
    path('register',views.Register_home,name='register'),
    path('registeration',views.Register_user,name='registeration'),
    path('signin',views.Donor_home,name='signin'),
    path('login/',views.Login, name='login'),



 # DONOR

 
    path('donor_home',views.donormain,name='donor_home'),
    path('Logout/',views.Logout, name='Logout'),
    path('eligibility/<int:userid>/',views.Eligibilitys, name='eligibility'),
    path('view',views.view,name='view'),

    path('profile',views.donor_profile, name='profile'),
    path('donor_edit',views.donor_edit, name='donor_edit'),

    path('view',views.qa_list, name='view'),




# RECIPIENT

     
    path('recipient',views.Recipient_login,name='recipient'),
    path('recipient_home',views.filter_donors, name='recipient_home'),
    path('recipient_profile',views.Recipient_profile, name='recipient_profile'),
    path('recipient_edit',views.Recipient_edit, name='recipient_edit'),
    path('click/<int:donor_id>/',views.click, name='click'),


    

# Forgotpassword


    path('password_reset/',views.password_reset_request,name='password_reset'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_new_password',views.set_new_password,name='set_new_password'),


# notification

    
     path('send_donor', views.send_donor, name='send_donor'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

