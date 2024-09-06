from .models import Friendrequest,Traveller,Travellerinfo

from rest_framework import serializers

class Travelerserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)

    class Meta:
        model = Traveller
        fields = ['id','first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password as it's not needed for creation
        user = Traveller(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class Travelerprofile(serializers.ModelSerializer):
    class Meta:
        model=Travellerinfo
        fields=['people','image','bio','phone','gender','city','fb','x']


class Friendrequestserializer(serializers.ModelSerializer):
    class Meta:
        model=Friendrequest
        fields='__all__'