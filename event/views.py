from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.conf import settings
from customer.models import Traveller
from rest_framework import status
# Create your views here.


class Travelviewset(viewsets.ModelViewSet):
     queryset=models.Travel.objects.all()
     serializer_class=serializers.Travelserializer


     def get_queryset(self):
          queryset= super().get_queryset()

          travel_id=self.request.query_params.get('travel_id')
          people=self.request.query_params.get('people')

          if travel_id:
               queryset=queryset.filter(travel_id=travel_id)
          if people:
              queryset=queryset.filter(people=people)

          return queryset

     

     @action(detail=True, methods=['post'])
     def addpeople(self,request,pk=None):
        travel_instance=get_object_or_404(models.Travel,id=pk)  
        traveler_count=travel_instance.people.count()
        if traveler_count< travel_instance.people_limit:
             user_id=request.data.get('user_id')
             user_account=get_object_or_404(Traveller,id=user_id)
             print(user_account)
             if  user_account in travel_instance.people.all():
               return Response('you already in the travel plan')
             else:    
                travel_instance.people.add( user_account)
                return Response ('congratulations you are in')
           
        else:
            return Response('Better Luck Next time')

        
     


class Reviewset(viewsets.ModelViewSet):
     queryset=models.Review.objects.all()
     serializer_class=serializers.Reviewserializer



     def get_queryset(self):
          queryset= super().get_queryset()

          travelname=self.request.query_params.get('travelname')
          reviewer=self.request.query_params.get('reviewer')

          if travelname:
               queryset=queryset.filter(travelname=travelname)
          if reviewer:
              queryset=queryset.filter(reviewer=reviewer)

          return queryset

     


    
class smsviewset(viewsets.ModelViewSet):
    queryset = models.sms.objects.all()
    serializer_class = serializers.smserializer



    def get_queryset(self):
          queryset= super().get_queryset()

          plan=self.request.query_params.get('plan')

          if plan:
               queryset=queryset.filter(plan=plan)
        
          return queryset

    @action(detail=True, methods=['post'])
    def sendmessage(self, request, pk=None):
        travel_instance = get_object_or_404(models.Travel,id=pk)  # Get the Travel instance using pk
        user = request.data.get('user_id')  # Get the user ID from request data
        sender = get_object_or_404(models.Traveller,id=user)
        print(sender)
        travel_instance.people.add(sender)
        text = request.data.get('text')  # Get the message text from request data
        
        # Find the existing sms instance or create a new one
        if travel_instance.people.filter(id=user).exists():
          print('hello')
          sms_instance = models.sms.objects.create(

             Text=text,
             plan=travel_instance
            )
          sms_instance.user.set([sender])
         
          return Response({'status': 'Message success'}, status=status.HTTP_201_CREATED)
        
        return Response({'status': 'Message failed to send'}, status=status.HTTP_201_CREATED)