from django.urls import path,include
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.listEvents, name="listEvents"),
    path('events/<event_id>', views.viewEvent, name='viewEvent'),
    path('post/<club_id>', views.postEvent, name="postEvent"),
    path('update/<event_id>', views.updateEvent, name='updateEvent'),
    path('delete/<event_id>', views.deleteEvent, name='deleteEvent'),
    path('register/<event_id>', views.registerAtEvent, name='registerAtEvent'),
]