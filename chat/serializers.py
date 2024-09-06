from rest_framework import serializers
from .models import sms,chatmodel

class smserializer(serializers.ModelSerializer):
    class Meta:
        model=sms
        fields='__all__'


class chatserializer(serializers.ModelSerializer):
    class Meta:
        model=chatmodel
        fields='__all__'