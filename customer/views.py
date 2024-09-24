from django.shortcuts import render
from customer.models import Traveller ,Friendrequest,Travellerinfo
from .serializers import Travelerserializer,Friendrequestserializer,Travelerprofile
from rest_framework import viewsets,status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .import serializers
from rest_framework.authtoken.models import Token
# from rest_framework.decorators import lo
from django.contrib.auth import authenticate
from rest_framework.decorators import  api_view


# Create your views here.

class Travellerviewset(viewsets.ModelViewSet):
    queryset=Traveller.objects.all()
    serializer_class=Travelerserializer
 
    @action(detail=False,methods=['Post']) 
    def newuser(self,request):
     serializer=self.get_serializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
         return Response ({'message':'Your registration is completed'},status=status.HTTP_201_CREATED)
     return Response ({'error':'Registration is not get well,Try again'},status=status.HTTP_400_BAD_REQUEST)
     

    @action(detail=False,methods=['Post']) 
    def login(self,request):
       if request.method == 'POST':  
        username=request.data.get('username')
        password=request.data.get('password')
        print(username,password)

        user=None

        if '@' in username:
            try:
                user=Traveller.objects.get(email=username)
                print(user)
                if not user.check_password(password):
                  user = None  
            except Traveller.ObjectDoesNotExist:
                pass
        
        if not user:
            user=authenticate(username=username,password=password)
        
        

        if user:
            token, _ = Token.objects.get_or_create(user=user)
           
            return Response({'token': token.key,'user_id':user.id}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


    @api_view(['POST'])
    def logout(self,request):
          if request.method == 'POST':
               try:
                      request.user.auth_token.delete()
                      return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
               except:
                      return Response({'error': 'Logout process donot go well.'}, status=status.HTTP_200_OK)
                   







class friendrequestviewset(viewsets.ModelViewSet):
    queryset=Friendrequest.objects.all()
    serializer_class=Friendrequestserializer
    
    @action(detail=False,methods=['post'])
    def send_request(self,request):
        sender=request.user
        to_user=request.data.get('to_user')
        userr=get_object_or_404(Traveller,id=int(to_user))
        if sender in userr.friends.all():
            return  Response('you are already friend')

        if int(sender.id)!=int(to_user): 
           if to_user:
        
                 reciever=Traveller.objects.get(id=to_user)
                 friend_request,created=Friendrequest.objects.get_or_create(from_user=sender, to_user=reciever)
                 if created:
                   return Response ('friendrequest sent')
                 else:
                   return Response('you already sent a request')
        else:
             return Response('usernot found')

    
    @action(detail=True,methods=['post'])
    def accept_request(self,request,pk):
        friend_request=Friendrequest.objects.get(id=pk)
        sender=request.data.get('from_user')
        reciever=request.data.get('to_user')
        print(sender,reciever)
        reciever=int(reciever)
        print(type(friend_request.to_user.id),type(reciever))
        if (friend_request.to_user.id==int(reciever)) and (friend_request.from_user.id==int(sender)):
            friend_request.to_user.friends.add(friend_request.from_user)
            friend_request.delete()
            return Response ('Request Accepted')
        else:
            return Response('Request is still Hanging')
        





    @action(detail=True,methods=['post'])
    def remove_request(self,request,pk):
        friend_request=Friendrequest.objects.get(id=pk)
        sender=request.data.get('from_user')
        reciever=request.data.get('to_user')
        print(sender,reciever)
        reciever=int(reciever)
        print(type(friend_request.to_user.id),type(reciever))
        if (friend_request.to_user.id==int(reciever)) and (friend_request.from_user.id==int(sender)):
            friend_request.delete()
            return Response ('Request deleted')
        else:
            return Response('Request is still Hanging')
             
    
    def get_queryset(self):
          queryset= super().get_queryset()

          to_user=self.request.query_params.get('to_user')

          if to_user:
               queryset=queryset.filter(to_user=to_user)
        
          return queryset
       

class addprofileinfo(viewsets.ModelViewSet):
    queryset=Travellerinfo.objects.all()
    serializer_class=Travelerprofile

     

    def get_queryset(self):
       queryset=super().get_queryset()
       people=self.request.query_params.get ('people')
       if  people:
           queryset=queryset.filter(people= people)
           return queryset
       queryset = super().get_queryset()
       people = self.request.query_params.get('people')

       if self.request.method == 'GET' and people:
            queryset = queryset.filter(people__id=people)  # Assuming 'people' is the ID

       return queryset


    # def list(self, request, *args, **kwargs):
    #     # Handle GET request to list profiles based on query parameter
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)  # Return a list of profiles

    # def retrieve(self, request, *args, **kwargs):
    #     # Handle GET request to retrieve a specific profile
    #     instance = self.get_object()  # Get the instance based on the provided ID
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)  # Return the serialized data

    # def update(self, request, *args, **kwargs):
    #     # Handle PUT request to update an existing profile completely
    #     instance = self.get_object()  # Get the instance to be updated
    #     serializer = self.get_serializer(instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()  # Save the updated profile
    #         return Response(serializer.data)  # Return the serialized data of the updated profile
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, *args, **kwargs):
    #     # This method will be called for PUT requests
    #     return self.update(request, *args, **kwargs)


# class updateprofileinfo(viewsets.ModelViewSet):
#      queryset=Travellerinfo.objects.all()
#      serializer_class=Travelerprofile

#      def get_queryset(self):
#        queryset=super().get_queryset()
#        people=self.request.query_params.get ('people')
#        if  people:
#            queryset=queryset.filter(people= people)
#            return queryset










    

