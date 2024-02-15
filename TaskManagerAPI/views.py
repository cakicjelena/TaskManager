from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.

#Registration
@api_view(['GET', 'POST'])
def create_user_view(request):
    if request.method=='POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        tempUser=User.objects.filter(email=request.POST.get('email'))
        if( tempUser):
            print(tempUser)
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

@csrf_exempt

def login_view(request):
    email=request.data.get('email')
    password=request.data.get('password')
    #print(email, password)
    user=authenticate(email=email, password=password)
    print(user)
    if (user):
        login(request, user)
        serializer=UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response("User not exist", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def login_template(request):
    return render(request, 'login.html')
