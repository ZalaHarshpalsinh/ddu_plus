from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']

class PersonInfoForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['profilePhoto', 'department']

class StudentInfoForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['semester']

class EmployeeInfoForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['designation']


