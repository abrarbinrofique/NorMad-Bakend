from django.db import models
from event.models import Travel
from customer.models import Traveller
from django.conf import settings
# Create your models here.

class sms(models.Model):
    Text=models.TextField()



class chatmodel(models.Model):
    travel=models.OneToOneField(Travel,null=True, blank=True , on_delete=models.CASCADE)
    user=models.ManyToManyField(Traveller,blank=True)
    message=models.ManyToManyField(sms)

