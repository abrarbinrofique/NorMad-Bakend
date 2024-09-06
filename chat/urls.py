from django.urls import path,include
from .import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('travelplan/',views.smsviewset)
router.register('chatbox/',views.chatviewset)



urlpatterns = [
 
    path("",include(router.urls)),
    
]
