from django.shortcuts import render
from .import models
from .import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from event.models import Travel
from rest_framework.decorators import action
from customer.models import Traveller
# Create your views here.

class shareviewset(viewsets.ModelViewSet):
    queryset=models.Sharetravel.objects.all()
    serializer_class=serializers.Sharetravelserializers
    


   
    @action(detail=True, methods=['post'])
    def sharetravel_add(self,request,pk):     
        isinstance_travel=get_object_or_404(models.Sharetravel,id=pk )
        main_travel=isinstance_travel.share
        user_id=request.data.get('user_id')
        isinstance_user=get_object_or_404(Traveller,id=user_id)
        if isinstance_user in isinstance_travel.travellersgroup.all() or isinstance_user in main_travel.people.all() :
            return Response ("You are already in the travel")
        else:
            traveler_count=isinstance_travel.travellersgroup.count()
            if traveler_count<isinstance_travel.peoplelimit:
                isinstance_travel.travellersgroup.add(isinstance_user)
               
                traveler_count=isinstance_travel.travellersgroup.count()
                if traveler_count==isinstance_travel.peoplelimit:
                    k= main_travel.people_limit-main_travel.people.count()
                    if k>=traveler_count:
                       for i in isinstance_travel.travellersgroup.all():
                           main_travel.people.add(i)
                       return Response({'message': 'Happy Journey!!!'})
                else:
                     return Response({'message': 'Watting for your other friends!!!'})
                   
            else:
                  return Response({'message': 'Sorry,This slot is fillup,check main slot'})

 
    

                           
                   


            






        