from rest_framework import serializers
from .models import User, Project, Task, UserOnProject, CommentOnTask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'first_name', 'last_name', 'email', 'password', 'sex', 'birthDate', 'is_staff', 'is_superuser')
    
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


'''class UserOnTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserOnTask
        fields=('taskId', 'userId', 'taskName', 'userName', 'startDate')'''

class CommentOnTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentOnTask
        fields=('taskId', 'email', 'comment')