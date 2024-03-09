from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('search', views.search, name='search'),
    path('users/<user_id>', views.userProfile, name='userProfile'),
    path('departments/<department_id>', views.departmentProfile, name='departmentProfile'),
]