from django.db import models

# Create your models here.
class Student(models.Model):
    Student_nm=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    mobile=models.IntegerField()

    def __str__(self):
        return self.Student_nm+' '+self.email
    
    class Meta:
        db_table="StudentTbl"

        #Admin panal pr s add kr k deta hai  ---> " Student1s "
        # verbose_name="Student1"

        # admin panal k name me baad me s nahi aayega ----->" Student "
        verbose_name_plural="Student"
        ordering=['Student_nm']
