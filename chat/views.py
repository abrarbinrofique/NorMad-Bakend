from django.shortcuts import render
from chat.models import sms,chatmodel
from chat.serializers import smserializer,chatserializer
from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.



class smsviewset(viewsets.ModelViewSet):
    queryset=sms.objects.all()
    serializer_class=smserializer


class chatviewset(viewsets.ModelViewSet):
    queryset=chatmodel.objects.all()
    serializer_class=chatserializer

   