from django.shortcuts import render,get_object_or_404,redirect
from authentication.models import *
from .forms import *
from django.db.models import Q

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


def departments(request):
    departments = Department.objects.all()

    return render(request, 'profiles/department_list.html', {
        'departments' : departments,
    })

def departmentProfile(request, department_id):
    department = get_object_or_404(Department, pk=department_id)

    return render(request, 'profiles/entity_profile.html', {
        'entity' : department,
    })

def clubs(request):
    clubs = Club.objects.all()

    return render(request, 'profiles/club_list.html', {
        'clubs' : clubs,
    })

def clubProfile(request, club_id):
    club = get_object_or_404(Club, pk=club_id)

    return render(request, 'profiles/entity_profile.html', {
        'entity' : club,
    })

    