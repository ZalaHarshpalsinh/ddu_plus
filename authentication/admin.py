from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Club)