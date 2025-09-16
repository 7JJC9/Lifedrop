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

urlpatterns = [
    path('admin/', admin.site.urls),

 # DONOR


    path('',views.Home,name=''),
    path('donor',views.Donor_home,name='donor'),
    # path('recipient',views.Recipient_home,name='recipient'),
    path('register',views.Donor_form,name='register'),
    path('donor_home',views.donormain,name='donor_home'),
    path('donor/',views.Login,name='donor'),
    path('Logout/',views.Logout, name='Logout'),
    path('eligibility',views.Eligibilitys, name='eligibility'),

    path('profile',views.donor_profile, name='profile'),
    path('donor_edit',views.donor_edit, name='donor_edit'),
     path('donor_delete/<int:id>',views.donor_delete, name='donor_delete'),


    path('view',views.qa_list, name='view'),




# RECIPIENT

    path('recipient',views.Recipient_serach, name='recipient'),


    

# Forgotpassword


    path('password_reset/',views.password_reset_request,name='password_reset'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_new_password',views.set_new_password,name='set_new_password'),
    
]



