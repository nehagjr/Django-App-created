from django.db import models

# Create your models here.
class Student(models.Model):
    Student_nm=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    mobile=models.IntegerField()
