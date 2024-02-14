from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, firstName=None, lastName=None, email=None, password=None, birthDate=datetime.now, sex=1, is_active=0, is_superuser=0, **extra_fields):
        user=self.model(email=email, **extra_fields)
        user.firstName=firstName
        user.lastName=lastName
        user.set_password(password)
        user.birthDate=birthDate
        print(user.birthDate)
        user.sex=sex
        user.is_active=is_active
        user.is_superuser=is_superuser
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    id=models.AutoField(unique=True, null=False, blank=False, primary_key=True)
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    birthDate=models.DateField()
    sex=models.IntegerField(default=1)
    is_active=models.IntegerField()
    is_superuser=models.IntegerField()

    objects=UserManager()
    def __str__(self):
        return self.email


class ProjectManager(models.Manager):
    def create_project(self, name=None, createDate=None, deadlineDate=None, description=None, projectManagerId=0, **extra_fields):
        project=self.model(name=name, **extra_fields)
        project.createDate=createDate
        project.deadlineDate=deadlineDate
        project.description=description
        project.projectManagerId=projectManagerId
        project.save(using=self._db)
        return project
    
class Project(models.Model):
    id=models.AutoField(unique=True,null=False, blank=False, primary_key=True )
    name=models.CharField(max_length=100)
    createDate=models.DateField()
    deadlineDate=models.DateField()
    description=models.CharField(max_length=500)
    projectManagerId= models.IntegerField(null=False, blank=False)

    objects=ProjectManager()
    def __str__(self):
        return self.name
    

class TaskManager(models.Manager):
    def create_task(self, name=None, type=0, desciption= None, status= 0, startDate= None, finishDate=None, projectId=0, userId=0, **extra_fields):
        task=self.model(name=name, **extra_fields)
        task.type=type
        task.description=desciption
        task.status=status
        task.startDate=startDate
        task.finishDate=finishDate
        task.projectId=projectId
        task.userId=userId
        task.save(using=self._db)
        return task
    
class Task(models.Model):
    id=models.AutoField(unique=True, null=False, blank=False, primary_key=True)
    name=models.CharField(max_length=100)
    type=models.IntegerField()
    description=models.CharField(max_length=500)
    status=models.IntegerField()
    startDate=models.DateField()
    finishDate=models.DateField()
    projectId=models.IntegerField(null=False, blank=False)
    userId=models.IntegerField(null=False, blank=False)

    objects=TaskManager()
    def __str__(self):
        return self.name
    
class UserOnProject(models.Model):
    projectId=models.IntegerField(null=False, blank=False)
    userId=models.IntegerField(null=False, blank=False)
    projectName=models.CharField(max_length=100)
    userName=models.CharField(max_length=100)
    startDate=models.DateField()

class ProjectTask(models.Model):
    projectId=models.IntegerField(null=False, blank=False)
    taskId=models.IntegerField(null=False, blank=False)
    projectName=models.CharField(max_length=100)
    taskName=models.CharField(max_length=100)

class UserOnTask(models.Model):
    taskId=models.IntegerField(null=False, blank= False)
    userId=models.IntegerField(null=False, blank=False)
    taskName=models.CharField(max_length=100)
    userName=models.CharField(max_length=100)
    startDate=models.DateField()

