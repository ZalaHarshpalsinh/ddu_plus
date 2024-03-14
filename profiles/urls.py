from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('users', views.users, name='users'),
    path('users/<user_id>', views.userProfile, name='userProfile'),
    path('departments/', views.departments, name='departments'),
    path('departments/<department_id>', views.departmentProfile, name='departmentProfile'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/<club_id>', views.clubProfile, name='clubProfile'),
]