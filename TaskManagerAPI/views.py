from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#Registration
@api_view(['GET', 'POST'])
def create_user_view(request):
    if request.method=='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        tempUser=User.objects.filter(email=request.POST.get('email'))
        if(tempUser is not None):
            return Response("User already exists", status=status.HTTP_400_BAD_REQUEST)
        email=request.POST.get('email')
        password=request.POST.get('password')
        birthDate=request.POST.get('birthDate')
        sex=request.POST.get('sex')
        is_active=request.POST.get('is_active')
        is_superuser=request.POST.get('is_superuser')
        user=User.objects.create_user(firstName, lastName, email, password, birthDate, sex, 0, is_superuser)
        serializer=UserSerializer(user)
        print(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method=='GET':
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
#Login
@api_view(['POST'])
def login_view(request):
    email=request.data.get('email')
    password=request.data.get('password')
    user=authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        serializer=UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

