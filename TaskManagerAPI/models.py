from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,first_name=None,last_name=None, sex=None, birthDate=None, **extra_fields):
        #if not email:
            #raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.first_name=first_name
        user.last_name=last_name
        user.sex=sex
        user.birthDate= birthDate
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email, password, extra_fields)

    

class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    sex=models.BooleanField(default=True)
    birthDate=models.DateField()
    is_active= models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

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
    
class UserOnProjectManager(models.Manager):
    def create_user_on_project(self, projectId=0, userId=0, projectName=None, userName=None, startDate=None, **extra_fields):
        user_on_project=self.model(projectName=projectName, **extra_fields)
        user_on_project.projectId=projectId
        user_on_project.userId=userId
        user_on_project.userName=userName
        user_on_project.startDate=startDate
        user_on_project.save(using=self._db)
        return user_on_project
    
class UserOnProject(models.Model):
    projectId=models.IntegerField(null=False, blank=False)
    userId=models.IntegerField(null=False, blank=False)
    projectName=models.CharField(max_length=100)
    userName=models.CharField(max_length=100)
    startDate=models.DateField()

    objects=UserOnProjectManager()

    def __str__(self):
        return self.projectName

class UserOnTasktManager(models.Manager):
    def create_user_on_task(self, taskId=0, userId=0, taskName=None, userName=None, startDate=None, **extra_fields):
        user_on_task=self.model(taskName=taskName, **extra_fields)
        user_on_task.taskId=taskId
        user_on_task.userId=userId
        user_on_task.userName=userName
        user_on_task.startDate=startDate
        user_on_task.save(using=self._db)
        return user_on_task

class UserOnTask(models.Model):
    taskId=models.IntegerField(null=False, blank= False)
    userId=models.IntegerField(null=False, blank=False)
    taskName=models.CharField(max_length=100)
    userName=models.CharField(max_length=100)
    startDate=models.DateField()

    objects=UserOnTasktManager()

    def __str__(self):
        return self.taskName


class CommentOnTasktManager(models.Manager):
    def create_comment_on_task(self, taskId=0, email=None, comment=None, **extra_fields):
        comment_on_task=self.model(email=email, **extra_fields)
        comment_on_task.taskId=taskId
        comment_on_task.comment=comment
        comment_on_task.save(using=self._db)
        return comment_on_task

class CommentOnTask(models.Model):
    taskId=models.IntegerField(null=False, blank= False)
    email=models.CharField(max_length=100)
    comment=models.CharField(max_length=500)

    objects=CommentOnTasktManager()

    def __str__(self):
        return self.email
    