from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class userTypes(models.TextChoices):
        STUDENT  = 'STUDENT', 'student'
        EMPLOYEE = 'EMPLOYEE', 'employee'
    
    type = models.CharField(max_length=8, choices=userTypes.choices, default=userTypes.STUDENT)

class Department(models.Model):
    profilePhoto = models.ImageField(upload_to='profile_photos/Departments')
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

class Person(models.Model):
    profilePhoto = models.ImageField(upload_to='profile_photos/People')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.username


class Student(models.Model):
    semesters = (
        ('1','1'),
        ('2','2'),
        ('3','3'), 
        ('4','4'), 
        ('5','5'), 
        ('6','6'), 
        ('7','7'), 
        ('8','8'),
        )
    semester = models.CharField(max_length=1, choices=semesters)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.account.username


class Employee(models.Model):
    designation = models.CharField(max_length=50)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.account.username




     
