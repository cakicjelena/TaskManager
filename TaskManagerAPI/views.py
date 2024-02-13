from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def api_home(request):
    print(request)
    if request.method=='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create_user(firstName, lastName, email, password)
        serializer=UserSerializer(user)
        print (user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method=='GET':
        return Response("Hello")
