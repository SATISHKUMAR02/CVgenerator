from django.db import models

# Create your models here.
class Profile(models.Model):
    
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    about=models.TextField(max_length=5000)

    school=models.CharField(max_length=200)
    college=models.CharField(max_length=200)

    experience=models.TextField(max_length=1000)
    skills=models.TextField(max_length=2000)
    def __str__(self):
        return self.name

""" 
username=>cvgen
cvgen@gmail.com
password=>cvgencvgen

"""
