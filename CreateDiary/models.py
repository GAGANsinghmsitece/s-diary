from django.db import models
from django.utils import timezone

class DiaryUser(models.Model):
	Username=models.CharField(max_length=30,unique=True)
	Password=models.CharField(max_length=30)
	CheckPassword=models.CharField(max_length=30,default='idiotitissameaspassword')



class DiaryText(models.Model):
	DiaryUser=models.CharField(max_length=30,unique=False)
	DateCreated=models.DateTimeField(default=timezone.now)
	DiaryBody=models.TextField(max_length=10000)
	DiaryHeading=models.CharField(max_length=50,unique=False,null=True)

class Profile(models.Model):
	Name=models.CharField(max_length=30,blank=True)
	DiaryUser=models.CharField(max_length=30,unique=False)
	Hobbies=models.TextField(max_length=120,blank=True)
	LivesAt=models.CharField(max_length=30,blank=True)
	WorksAt=models.CharField(max_length=30,blank=True)
	ProfilePic=models.ImageField(upload_to='UserAvatar')



# Create your models here.
