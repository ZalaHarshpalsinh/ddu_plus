from django import forms
from authentication.models import *
from events.models import *
from authentication.forms import *

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class DepartmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'about', 'profilePhoto']

class ClubUpdateForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'about', 'profilePhoto']




