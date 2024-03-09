from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *

# Create your views here.
def studentRegister(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        personForm = PersonInfoForm(request.POST , request.FILES)
        studentForm = StudentInfoForm(request.POST)

        if userForm.is_valid() and personForm.is_valid() and studentForm.is_valid() :
            user = userForm.save()
            person = personForm.save(False)
            person.account = user
            person.save()
            student = studentForm.save(False)
            student.person = person
            student.save()

            return redirect('landingPage')
    else:
        userForm = UserRegistrationForm()
        personForm = PersonInfoForm()
        studentForm = StudentInfoForm()

    return render(request, 'authentication/student/register.html', {
        'userForm' : userForm,
        'personForm' : personForm,
        'studentForm' : studentForm,
    }) 


def employeeRegister(request):
    if request.method == 'POST':
        userForm = UserRegistrationForm(request.POST)
        personForm = PersonInfoForm(request.POST, request.FILES)
        employeeForm = EmployeeInfoForm(request.POST)

        if userForm.is_valid() and personForm.is_valid() and employeeForm.is_valid() :
            user = userForm.save(False)
            user.type = user.userTypes.EMPLOYEE
            user.save()
            person = personForm.save(False)
            person.account = user
            person.save()
            employee = employeeForm.save(False)
            employee.person = person
            employee.save()

            return redirect('landingPage')
    else:
        userForm = UserRegistrationForm()
        personForm = PersonInfoForm()
        employeeForm = EmployeeInfoForm()

    return render(request, 'authentication/employee/register.html', {
        'userForm' : userForm,
        'personForm' : personForm,
        'employeeForm' : employeeForm,
    }) 

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request ,user)
                return redirect('landingPage')
    else:
        form = AuthenticationForm()

    return render(request, 'authentication/login.html', {
        'form' : form,
    })


def logoutView(request):
    logout(request)
    return redirect('landingPage')
