from rest_framework import serializers
from .import models


class Sharetravelserializers(serializers.ModelSerializer):
   class Meta: 
    model=models.Sharetravel
    fields='__all__'