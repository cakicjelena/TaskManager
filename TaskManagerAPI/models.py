from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,first_name=None,last_name=None, sex=None, birthDate=None, is_superuser=False, **extra_fields):
        #if not email:
            #raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.first_name=first_name
        user.last_name=last_name
        user.sex=sex
        user.birthDate= birthDate
        user.is_superuser=is_superuser
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
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

class Project(models.Model):
        name = models.CharField(max_length = 150)
        users = models.ManyToManyField(User)
        createDate=models.DateField()
        deadlineDate=models.DateField()
        description=models.CharField(max_length=500)
        projectManagerId= models.IntegerField(null=False, blank=False)

        def __str__(self):
          return self.name

class CommentOnTask(models.Model):
    #taskId=models.IntegerField(null=False, blank= False)
    email=models.CharField(max_length=100)
    comment=models.CharField(max_length=500)

    

    def __str__(self):
        return self.email


class Task(models.Model):
      name = models.CharField(max_length = 150)
      project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=False
    )
      user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False
    )
      type=models.IntegerField()
      description=models.CharField(max_length=500)
      status=models.IntegerField()
      startDate=models.DateField()
      finishDate=models.DateField()
      comments = models.ManyToManyField(CommentOnTask)
      
      def __str__(self):
        return self.name
    
