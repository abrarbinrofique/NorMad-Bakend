from django.contrib import admin
from django.urls import path,include
from .import views 

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('friendrequest',views.friendrequestviewset)
router.register('registration',views.Travellerviewset)
router.register('upgrade',views.addprofileinfo)

urlpatterns = [
   
 
    path("",include(router.urls)),
    
]
