from django.contrib import admin
from .models import *

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    filter_horizontal = ['admins']

class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ['participants']

admin.site.register(Club, ClubAdmin)
admin.site.register(Event, EventAdmin)