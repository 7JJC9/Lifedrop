from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('donor', 'Donor'),
        ('recipient', 'Recipient'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='donor')

    def __str__(self):
        return f"{self.username} ({self.role})"


# Create your models here.
class Donors(models.Model):
    userid = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=50)
    mob=models.IntegerField()
    bloodgroup=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=50)
    donateddate=models.DateField(null=True, blank=True)
    certificate=models.FileField(upload_to='media/certificates/', null=True, blank=True)

class Recipient(models.Model):
    userid = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fname=models.CharField(max_length=50 , default='Unknown')
    lname=models.CharField(max_length=50 , default='Unknown')
    dob=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=50)
    mob=models.IntegerField()
    bloodgroup=models.CharField(max_length=50 , default='Unknown')
    age=models.IntegerField()
    address=models.CharField(max_length=100 , default='Unknown')
    district=models.CharField(max_length=50, default='Not specified')
    wgroup=models.CharField(max_length=50)
    wdistrict=models.CharField(max_length=50)
    wgender=models.CharField(max_length=50)


class Eligibility(models.Model):

    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
           # questions=models.CharField(max_length=200)

    ans1=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans2=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans3=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans4=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans5=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans6=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans7=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans8=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans9=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans10=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans11=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans12=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans13=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans14=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans15=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans16=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans17=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans18=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans19=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')
    ans20=models.CharField(max_length=3 , choices=[('Yes','Yes'), ('No','No')], default='Nill')

    def __str__(self):
        return f"Eligibility for {self.userid}"




   



class Info(models.Model):
     userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     group=models.CharField(max_length=50)
     donors=models.CharField(max_length=50)
     recipient=models.CharField(max_length=50)



class Notification(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.recipient} -> {self.donor}"



    


  

