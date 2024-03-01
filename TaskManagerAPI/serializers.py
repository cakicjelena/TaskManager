from rest_framework import serializers

from .models import User, Project, Task, CommentOnTask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'first_name', 'last_name', 'email', 'password', 'sex', 'birthDate', 'is_staff', 'is_superuser')


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many = True)
    class Meta:
        model=Project
        fields=('id', 'name', 'users', 'createDate', 'deadlineDate', 'description', 'projectManagerId')

class CommentOnTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentOnTask
        fields=('email', 'comment')         

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = CommentOnTaskSerializer(many = True)
    class Meta:
        model=Task
        fields=('id', 'name', 'project', 'user', 'type', 'description', 'status', 'startDate', 'finishDate','comments')
        