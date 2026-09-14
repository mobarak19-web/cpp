from django.db import models
# from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings


class CustomUser(AbstractUser):
   display_name = models.CharField(max_length=255)
   otp = models.IntegerField(null= True, blank=True)



class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    course=models.CharField(max_length=100)
    semester=models.IntegerField()
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add= True)
    profile_pic = models.ImageField(upload_to='media/',null=True)


    def __str__ (self):
     return self.name

#teacher list
class teacher(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add= True)

    def __str__ (self):
     return self.name


#student and teacher eksathe choise korte pare 

ROLE_CHOICES =(
   ('student' , 'Student'),
   ('teacher', 'Teacher'),
)
class Profile(models.Model):
   user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
   
   role = models.CharField(max_length=20 , choices=ROLE_CHOICES, default='student')
def __str__(self):
   return "{}" .format(self.user.username,self.role)

# staff item 
class staff(models.Model):
   name = models.CharField(max_length=255)
   department = models.CharField(max_length=255)


class Alumni(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
   

   
