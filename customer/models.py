from django.db import models
from django.contrib.auth.models import AbstractUser,User,Group,Permission
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
# Create your models here.
Gender_types={
    ('Male','Male'),
    ('Female','Female')
}

class Friendrequest(models.Model):
    from_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='sender',on_delete=models.CASCADE)
    to_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='reciever',on_delete=models.CASCADE)






class Traveller(AbstractUser):
       email = models.EmailField(unique=True)
       friends = models.ManyToManyField('self', symmetrical=True, blank=True)
       groups = models.ManyToManyField(
    Group,
    related_name='traveller_groups',  # Unique related_name
    blank=True)

       user_permissions = models.ManyToManyField(
    Permission,
    related_name='traveller_permissions',  # Unique related_name
    blank=True)
   



       def __str__(self):
           return self.username
    






    
class Travellerinfo(models.Model):
    people=models.OneToOneField(Traveller,on_delete=models.CASCADE)
    image=CloudinaryField('image', null=True, blank=True)
    bio=models.TextField()
    gender=models.CharField(choices=Gender_types,max_length=15,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    city=models.CharField(max_length=20)
    fb=models.CharField(max_length=100)
    x=models.CharField(max_length=100)



