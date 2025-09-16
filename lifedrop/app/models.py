from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donors(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
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
    # certificate=models.ImageField()

class Recipient(models.Model):
    name=models.CharField(max_length=50)
    mob=models.IntegerField()
    wgroup=models.CharField(max_length=50)
    wdistrict=models.CharField(max_length=50)
    wgender=models.CharField(max_length=50)


class Eligibility(models.Model):
    userid=models.ForeignKey(Donors,on_delete=models.CASCADE)
    questions=models.CharField(max_length=200)
    answers=models.BooleanField()

    def __str__(self):
        return self.questions[:200] 



class Info(models.Model):
     userid=models.ForeignKey(Donors,on_delete=models.CASCADE)
     group=models.CharField(max_length=50)
     donors=models.CharField(max_length=50)
     recipient=models.CharField(max_length=50)




    


  

