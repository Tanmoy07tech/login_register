from django.db import models

# Create your models here.
from django.db import models
from django import forms
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50,null=False)
    college_id=models.CharField(max_length=50,primary_key=True)
    email=models.EmailField(max_length=100,null=False,unique=True)
    password=models.CharField(max_length=12,null=False)

    def __str__(self):
        return self.college_id

