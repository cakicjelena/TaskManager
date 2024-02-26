from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .models import User, Task, Project, CommentOnTask, UserOnProject
from .serializers import UserSerializer, TaskSerializer, ProjectSerializer, CommentOnTaskSerializer, UserOnProjectSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.decorators import login_required


# Create your views here.

#Registration
@api_view(['POST'])
@csrf_exempt
def create_user_view(request):
    
    email=request.POST.get('email')
    password=request.POST.get('password')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    sex=request.POST.get('sex')
    birthDate=request.POST.get('birthDate')
    is_superuser=request.POST.get('is_superuser')
    user=User.objects.create_user(email, password, first_name, last_name, sex, birthDate, is_superuser)
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

#Logout
@api_view(['POST'])
@login_required
@csrf_exempt
def logout_view(request):
    logout(request)
    return Response({'User logout'}, status=status.HTTP_200_OK)

#Edit profile
@api_view(['POST'])
@login_required
@csrf_exempt
def edit_profile_view(request, upk):
    user=User.objects.get(id=upk)
    email=request.POST.get('email')
    password=request.POST.get('password')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    if(email!=""):
        user.email=email
    if(password!=""):
        user.set_password(password)
    if(first_name!=""):
        user.first_name=first_name
    if(last_name!=""):
        user.last_name=last_name
    user.save()
    return Response("Successfuly changed", status=status.HTTP_200_OK)


#Create project
@api_view(['POST'])
#@login_required
@csrf_exempt
def create_project_view(request):
    name=request.POST.get('name')
    createDate=request.POST.get('createDate')
    deadlineDate=request.POST.get('deadlineDate')
    description=request.POST.get('description')
    projectManagerId=request.POST.get('projectManagerId')

    project=Project.objects.create_project( name, createDate, deadlineDate, description, projectManagerId)
    serializer=ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Edit project
@api_view
@csrf_exempt
#@login_required
def edit_project_view(request, ppk):
    project=Project.objects.get(id=ppk)
    description=request.POST.get('description')
    deadlineDate=request.POST.get('deadlineDate')
    projectManagerId=request.POST.get('projectManagerId')
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
@csrf_exempt
def create_task_view(request):
    print(request)
    name=request.POST.get('name')
    type=request.POST.get('type')
    description=request.POST.get('description')
    statuss=request.POST.get('status')
    startDate=request.POST.get('startDate')
    finishDate=request.POST.get('finishDate')
    projectId=request.POST.get('projectId')
    userId=request.POST.get('userId')

    task=Task.objects.create_task( name, type, description, statuss, startDate, finishDate, projectId, userId)
    serializer=TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Put user on project
@api_view(['POST'])
@login_required
@csrf_exempt
def create_user_on_project(request, upk, ppk):
    u=User.objects.get(id=upk)
    p=Project.objects.get(id=ppk)
    uop=UserOnProject.objects.create_user_on_project(ppk, upk, p.name, u.email, "2024-02-20")
    serializer=UserOnProjectSerializer(uop)
    return Response("Succesfuly put user on project", status=status.HTTP_200_OK)
    
#Put user on task
'''@api_view(['POST'])
@csrf_exempt
def create_user_on_task(request, upk, tpk):
    u=User.objects.get(id=upk)
    t=Task.objects.get(id=tpk)
    uot=UserOnTask.objects.create_user_on_task(tpk, upk, t.name, u.email, "2024-02-20")
    serializer=UserOnProjectSerializer(uot)
    return Response("Succesfuly put user on task", status=status.HTTP_200_OK)'''

#Put comment on task
@api_view(['POST'])
@login_required
@csrf_exempt
def create_comment_on_task(request, upk, tpk):
    u=User.objects.get(id=upk)
    t=Task.objects.get(id=tpk)
    comment_on_task=request.POST.get('comment_on_task')
    comment=CommentOnTask.objects.create_comment_on_task(tpk, u.email, comment_on_task)
    serializer=CommentOnTaskSerializer(comment)
    return Response("Succesfuly put comment on task", status=status.HTTP_200_OK)

#List all users
@api_view(['GET'])
#@login_required
@csrf_exempt
def get_all_users(request):
    user=User.objects.all()
    serializer=UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#List all projects
@api_view(['GET'])
#@login_required
@csrf_exempt
def get_all_projects(request):
    project=Project.objects.all()
    serializer=ProjectSerializer(project, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all projects of user
@api_view(['GET'])
@login_required
@csrf_exempt
def get_all_projects_of_user(request, upk):
    projects=UserOnProject.objects.filter(userId=upk)
    serializer=UserOnProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all tasks of project
@api_view(['GET'])
#@login_required
@csrf_exempt
def get_all_tasks_of_project(request, ppk):
    tasks=Task.objects.filter(projectId=ppk)
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#List all tasks of user
@api_view(['GET'])
@login_required
@csrf_exempt
def get_all_tasks_of_user(request, upk):
    tasks=Task.objects.filter(userId=upk)
    serializer=TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#Change task status
@api_view(['POST'])
@csrf_exempt
@login_required
def change_task_status(request, tpk):
    task=Task.objects.get(id=tpk)
    task.status=request.POST.get('status')
    task.save()
    return Response("Status of task succesfully changed", status=status.HTTP_200_OK)


#Delete project
@api_view(['DELETE'])
@csrf_exempt
#@login_required
def delete_project(request, ppk):
    project=Project.objects.get(id=ppk)
    uop=UserOnProject.objects.filter(projectId=ppk)
    top=Task.objects.filter(projectId=ppk)
    top.delete()
    uop.delete()
    project.delete()
    return Response("Succesfully deleted project", status=status.HTTP_200_OK)

#Delete task
@api_view(['DELETE'])
@csrf_exempt
#@login_required
def delete_task(request, tpk):
    task=Task.objects.get(id=tpk)
    comment=CommentOnTask.objects.filter(taskId=tpk)
    comment.delete()
    task.delete()
    return Response("Succesfully deleted task", status=status.HTTP_200_OK)

#Delete user
@api_view(['DELETE'])
@csrf_exempt
@login_required
def delete_user(request, upk):
    user=User.objects.get(id=upk)
    uop=UserOnProject.objects.filter(userId=upk)
    uop.delete()
    uot=Task.objects.filter(userId=upk)
    uot.update(userId=-1)
    user.delete()
    return Response("Succesfully deleted user", status=status.HTTP_200_OK)


