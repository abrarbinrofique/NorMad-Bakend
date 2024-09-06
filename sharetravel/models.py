from django.db import models
from event.models import Travel
from django.contrib.auth.models import User
from django.conf import settings
from customer.models import Traveller
# Create your models here.
class Sharetravel(models.Model):
    share=models.ForeignKey(Travel,related_name='Maintravel', on_delete=models.CASCADE)
    peoplelimit=models.IntegerField()
    travellersgroup=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
    text=models.TextField(blank=True,null=True)
    shareby=models.ForeignKey(Traveller,related_name='sharebywho',null=True,blank=True,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.share