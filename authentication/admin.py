from django.contrib import admin
from .models import *

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    filter_horizontal = ['admins']

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Department, DepartmentAdmin)
