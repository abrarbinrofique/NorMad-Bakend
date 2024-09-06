from django.db import models
from cloudinary.models import CloudinaryField
from customer.models import Traveller
from django.conf import settings
# Create your models here.
STAR_CHOICE={
   ( 1,'⭐'),
    (2,'⭐⭐'),
    (3,'⭐⭐⭐'),
    (4,'⭐⭐⭐⭐'),
    (5,'⭐⭐⭐⭐⭐')
}


class Travel(models.Model):
    location=models.CharField(max_length=20)
    traveldate=models.DateField()
    time=models.TimeField()
    Description=models.TextField()
    cost=models.IntegerField()
    people=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    people_limit=models.IntegerField()


    def __str__(self):
        return self.location



# class Reviewtravel(models.Model):

class Review(models.Model):
    reviewer=models.ManyToManyField(settings.AUTH_USER_MODEL)
    ratting=models.IntegerField(choices=STAR_CHOICE)
    travelname=models.ForeignKey(Travel, on_delete=models.CASCADE)
    textreview=models.TextField() 




class sms(models.Model):
    Text=models.TextField()
    user=models.ManyToManyField(Traveller)
    plan=models.ForeignKey(Travel,null=True, blank=True , on_delete=models.CASCADE)

