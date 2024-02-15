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
@api_view(['POST'])
@csrf_exempt
def create_user_view(request):
    
    email=request.POST.get('email')
    password=request.POST.get('password')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    user=User.objects.create_user(email, password, first_name, last_name)
    serializer=UserSerializer(user)
    #if serializer.is_valid():
        #serializer.save()
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
    #else:
    return Response(serializer.data,status=status.HTTP_200_OK)
   
    
#Login
@api_view(['POST'])

@csrf_exempt

def login_view(request):
    email=request.data.get('email')
    password = request.data.get('password')
    user=authenticate(request, email=email, password=password)
    if user is not None:
        #token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        serializer= UserSerializer(user)
        #renderer_classes = [TemplateHTMLRenderer]
        #request.session['_old_post'] = request.POST  
        request.session['user'] = serializer.data 
        if serializer.data['is_staff'] is False:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Nesto")
               

        #return redirect("homeUser")
        #return Response({
            #'token': token.key,
            #'user_id': user.id,
            #'email': user.email
        #})
    
    else:
        return Response({'error': 'Invalid email or password'}, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def login_template(request):
    return render(request, 'login.html')
