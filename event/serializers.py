from rest_framework import serializers
from .models import  Travel,Review,sms


class Travelserializer(serializers.ModelSerializer):
    class Meta:
        model=Travel
        fields=['id','location','traveldate','time','Description','cost','image','people_limit','people']


class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'


class smserializer(serializers.ModelSerializer):
    class Meta:
        model=sms
        fields='__all__'

