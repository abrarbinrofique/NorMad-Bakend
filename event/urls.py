from django.contrib import admin
from django.urls import path,include
from .import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('list',views.Travelviewset)
router.register('review',views.Reviewset)
router.register('travelplan',views.smsviewset)





urlpatterns = [
 
    path("",include(router.urls)),
    
]