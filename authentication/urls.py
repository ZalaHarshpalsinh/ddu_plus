from django.urls import path,include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('student/register', views.studentRegister, name='studentRegister'),
    path('employee/register', views.employeeRegister, name='employeeRegister'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
]