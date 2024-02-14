from rest_framework import serializers
from .models import User, Project, Task, UserOnProject, ProjectTask, UserOnTask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'firstName', 'lastName', 'email', 'password', 'birthDate', 'sex', 'is_active', 'is_superuser')
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id', 'name', 'createDate', 'deadlineDate', 'description', 'projectManagerId')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('id', 'name', 'type', 'description', 'status', 'startDate', 'finishDate', 'projectId', 'userId')

class UserOnProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserOnProject
        fields=('projectId', 'userId', 'projectName', 'userName', 'startDate')

class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectTask
        fields=('projectId', 'taskId', 'projectName', 'taskName')

class UserOnTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserOnTask
        fields=('taskId', 'userId', 'taskName', 'userName', 'startDate')