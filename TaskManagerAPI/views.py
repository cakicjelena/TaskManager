from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import User, Task, Project, CommentOnTask 
from .serializers import UserSerializer, TaskSerializer, ProjectSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


# Create your views here.

#Registration
@csrf_exempt
@api_view(['POST'])
def create_user_view(request):
    print (request.data.get('first_name'))
    email=request.data.get('email')
    password=request.data.get('password')
    first_name=request.data.get('first_name')
    last_name=request.data.get('last_name')
    sex=request.data.get('sex')
    birthDate=request.data.get('birthDate')
    is_superuser=request.data.get('is_superuser')
    user=User.objects.create_user(email, password, first_name, last_name, sex, birthDate, is_superuser)
    serializer=UserSerializer(user)
    return Response(serializer.data,status=status.HTTP_200_OK)
   
    
#Login
@api_view(['POST'])
def login_view(request):
    email=request.data.get('email')
    password = request.data.get('password')
    user=authenticate(request, email=email, password=password)
    if user is not None:
        #token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        serializer= UserSerializer(user)   
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid email or password'}, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def login_template(request):
    return render(request, 'login.html')

#Logout
@api_view(['POST'])
#@login_required
def logout_view(request):
    logout(request)
    return Response({'User logout'}, status=status.HTTP_200_OK)

#Edit profile

@api_view(['POST'])
@csrf_exempt
#@login_required
def edit_profile_view(request, upk):
    user=User.objects.get(id=upk)
    email=request.data.get('email')
    password=request.data.get('password')
    first_name=request.data.get('first_name')
    last_name=request.data.get('last_name')
    print(email)
    if(email!=None and email!=""):
        user.email=email
    if(password!=None and password!=""):
        user.set_password(password)
    if(first_name!=None and first_name!=""):
        user.first_name=first_name
    if(last_name!=None and last_name!=""):
        user.last_name=last_name
    user.save()
    serializer=UserSerializer(user)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Create project
@api_view(['POST'])
#@csrf_exempt
#@login_required
def create_project_view(request):
    print(request.data.get('createDate'))
    print(request.data.get('deadlineDate'))

    namep=request.data.get('name')
    createDate=request.data.get('createDate')
    deadlineDate=request.data.get('deadlineDate')
    description=request.data.get('description')
    projectManagerId=request.data.get('projectManagerId')

    project=Project.objects.create( name=namep, createDate=createDate, deadlineDate=deadlineDate, description=description, projectManagerId=projectManagerId)
    serializer=ProjectSerializer(project)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Edit project
@api_view(['POST'])
@csrf_exempt
#@login_required
def edit_project_view(request, ppk):
    project=Project.objects.get(id=ppk)
    description=request.data.get('description')
    deadlineDate=request.data.get('deadlineDate')
    projectManagerId=request.data.get('projectManagerId')
    if(description!=""):
        project.description=description
    if(deadlineDate!=""):
        project.deadlineDate=deadlineDate
    if(projectManagerId!=""):
        project.projectManagerId=projectManagerId
    project.save()
    return Response("Successfuly changed", status=status.HTTP_200_OK)


#Create task
@api_view(['POST'])
#@login_required
def create_task_view(request, ppk, upk):
    project1=Project.objects.get(id=ppk)
    user1=User.objects.get(id=upk)
    name=request.data.get('name')
    type=request.data.get('type')
    description=request.data.get('description')
    statuss=request.data.get('status')
    startDate=request.data.get('startDate')
    finishDate=request.data.get('finishDate')

    task=Task.objects.create( name=name, project=project1, user=user1, type=type, description=description, status=statuss, startDate=startDate, finishDate=finishDate)
    serializer=TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)

#edit task
@api_view(['POST'])
@csrf_exempt
#@login_required
def edit_task(request, tpk):
    task=Task.objects.get(id=tpk)
    name=request.data.get('name')
    description=request.data.get('description')
    finishDate=request.data.get('finishDate')
    userId=request.data.get('user')
    user=User.objects.get(id=userId)
    if(name!=""):
        task.name=name
    if(description!=""):
        task.description=description
    if(finishDate!=""):
        task.finishDate=finishDate
    if(user!=""):
        task.user=user
    task.save()
    return Response("Successfuly changed", status=status.HTTP_200_OK)


#Put user on project
@api_view(['POST'])
#@login_required
def create_user_on_project(request, upk, ppk):
    u=User.objects.get(id=upk)
    p=Project.objects.get(id=ppk)
    p.users.add(u)
    serializer=ProjectSerializer(p)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
#Put comment on task
@api_view(['POST'])
#@login_required
def create_comment_on_task(request, upk, tpk):
    u=User.objects.get(id=upk)
    t=Task.objects.get(id=tpk)
    comment_on_task=request.data.get('comment')
    comment=CommentOnTask.objects.create(email=u.email, comment=comment_on_task)
    t.comments.add(comment)
    serializer=CommentOnTaskSerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all users
@api_view(['GET'])
#@login_required
def get_all_users(request):
    user=User.objects.all()
    serializer=UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#List all projects
@api_view(['GET'])
#@login_required
def get_all_projects(request):
    project=Project.objects.all()
    serializer=ProjectSerializer(project, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all projects of user
@api_view(['GET'])
#@login_required
def get_all_projects_of_user(request, upk):
    user1=User.objects.get(id=upk)
    projects=Project.objects.filter(users=user1)
    serializer=ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all tasks of project
@api_view(['GET'])
#@login_required
def get_all_tasks_of_project(request, ppk):
    tasks=Task.objects.filter(project=ppk)
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all tasks of user
@api_view(['GET'])
#@login_required
def get_all_tasks_of_user(request, upk):
    tasks=Task.objects.filter(user=upk)
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Change task status
@api_view(['POST'])
#@login_required
def change_task_status(request, tpk):
    task=Task.objects.get(id=tpk)
    task.status=request.data.get('status')
    serializer=TaskSerializer(task)
    task.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


#List all comments
@api_view(['GET'])
#@login_required
def get_all_comments(request):
    comment=CommentOnTask.objects.all()
    serializer=CommentOnTaskSerializer(comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all comments of task
@api_view(['GET'])
#@login_required
def get_all_comments_of_task(request, tpk):
    task=Task.objects.get(id=tpk)
    comments=task.comments
    serializer=CommentOnTaskSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Delete project
@api_view(['DELETE'])
#@login_required
def delete_project(request, ppk):
    project=Project.objects.get(id=ppk)
    project.delete()
    return Response("Succesfully deleted project", status=status.HTTP_200_OK)

#Delete task
@api_view(['DELETE'])
#@login_required
def delete_task(request, tpk):
    task=Task.objects.get(id=tpk)
    task.delete()
    return Response("Succesfully deleted task", status=status.HTTP_200_OK)

#Delete user
@api_view(['DELETE'])
#@login_required
def delete_user(request, upk):
    user=User.objects.get(id=upk)
    user.delete()
    return Response("Succesfully deleted user", status=status.HTTP_200_OK)


