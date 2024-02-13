from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, firstName=None, lastName=None, email=None, password=None, **extra_fields):
        user=self.model(email=email, **extra_fields)
        user.firstName=firstName
        user.lastName=lastName
        user.set_password(password)
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    id=models.AutoField(unique=True, null=False, blank=False, primary_key=True)
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

    objects=UserManager()
    def __str__(self):
        return self.email
