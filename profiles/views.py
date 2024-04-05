from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from authentication.models import *
from .forms import *
from events.forms import *

# Create your views here.

def users(request):
    if request.method == "POST":
        key = request.POST['searchKey']
        users = User.objects.filter(Q(username__icontains = key) | Q(first_name__icontains = key) | Q(last_name__icontains = key))

        return render(request, 'profiles/user_list.html', {
            'users' : users,
        })

def userProfile(request, user_id):
    user = get_object_or_404(User,pk=user_id)

    if user.type == 'STUDENT':
        template = 'profiles/student_profile.html'
        extra = StudentInfoForm(instance=request.user.person.student)
    else :
        template = 'profiles/employee_profile.html'
        extra = EmployeeInfoForm(instance=request.user.person.employee)

    return render(request, template, {
        'user' : user,
        'update_form' : {
            'user': UserUpdateForm(instance=request.user),
            'person': PersonInfoForm(instance=request.user.person),
            'extra': extra,
        },
    })


def userUpdate(request):
    if request.method == "POST":
        userForm = UserUpdateForm(request.POST, instance=request.user)
        personForm = PersonInfoForm(request.POST, request.FILES, instance=request.user.person )
        if request.user.type == request.user.userTypes.STUDENT:
            additionalForm = StudentInfoForm(request.POST, instance=request.user.person.student)
        else:
            additionalForm = EmployeeInfoForm(request.POST, instance=request.user.person.employee)

        if userForm.is_valid() and personForm.is_valid() and additionalForm.is_valid() :
            userForm.save()
            personForm.save()
            additionalForm.save()
            return redirect('profiles:userProfile',request.user.id)

def userDelete(request):
    request.user.delete()
    return redirect('landingPage')

def departments(request):
    departments = Department.objects.all()

    return render(request, 'profiles/department_list.html', {
        'departments' : departments,
    })


def departmentProfile(request, department_id):
    department = get_object_or_404(Department, pk=department_id)

    isAdmin = False
    if request.user in department.admins.all():
        isAdmin = True
    
    form = DepartmentUpdateForm(instance=department)
    return render(request, 'profiles/department_profile.html', {
        'department' : department,
        'form': form,
        'isAdmin': isAdmin,
    })

def departmentUpdate(request, department_id):
    if request.method == "POST":
        department = Department.objects.get(id=department_id)
        form = DepartmentUpdateForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            form.save()
            return redirect('profiles:departmentProfile', department_id)

def clubs(request):
    clubs = Club.objects.all()

    return render(request, 'profiles/club_list.html', {
        'clubs' : clubs,
    })

def clubProfile(request, club_id):
    club = get_object_or_404(Club, pk=club_id)

    isAdmin = False
    if request.user in club.admins.all():
        isAdmin = True

    profile_form = ClubUpdateForm(instance=club)
    event_form = EventCreationForm()
    return render(request, 'profiles/club_profile.html', {
        'club' : club,
        'profile_form': profile_form,
        'event_form': event_form,
        'isAdmin':isAdmin,
    })

def clubUpdate(request, club_id):
    if request.method == "POST":
        club = Club.objects.get(id=club_id)
        form = ClubUpdateForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            form.save()
            return redirect('profiles:clubProfile', club_id)
    