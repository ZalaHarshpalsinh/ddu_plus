from django.shortcuts import render,get_object_or_404
from authentication.models import *
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
    else :
        template = 'profiles/employee_profile.html'

    return render(request, template, {
        'user' : user,
    })

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

    