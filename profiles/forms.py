from django import forms
from authentication.models import *
from authentication.forms import *

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



