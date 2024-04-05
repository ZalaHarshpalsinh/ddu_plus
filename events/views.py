from django.shortcuts import render,redirect,get_object_or_404
import json
from .models import *
from .forms import *

# Create your views here.
def listEvents(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {
        'events':events,
    })
    pass

def postEvent(request, club_id):
    if request.method == 'POST':

        club = get_object_or_404(Club, pk=club_id)
        form = EventCreationForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(False)
            event.club = club
            event.save()
            return redirect('events:listEvents')


def updateEvent(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(id=event_id)
        form = EventCreationForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:viewEvent', event_id)

def deleteEvent(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=event_id)
        event.delete()
        return redirect('events:listEvents')


def viewEvent(request, event_id):

    event = get_object_or_404(Event, pk=event_id)

    isAdmin = False

    if request.user in event.club.admins.all():
        isAdmin = True
        updateForm = EventCreationForm(instance=event)
        participants = event.participants.all()

        departmentData = [['Department', 'Count']]
        semesterData = [['Semester', 'Count']]
        userTypeData = [['UserType', 'Count']]

        departments = Department.objects.all()
        for department in departments:
            count = sum(1 for i in participants if i.person.department == department)
            data = [department.name, count]
            departmentData += [data]

        for semester in range(1,9):
            count = sum(1 for i in participants if i.type == 'STUDENT' and i.person.student.semester == str(semester))
            data = [str(semester), count]
            semesterData += [data]
        
        userTypes = ['STUDENT', 'EMPLOYEE']
        for type in userTypes:
            count = sum(1 for i in participants if i.type == type)
            data = [type, count]
            userTypeData += [data]

        return render(request, 'events/view_event.html', {
            'event': event,
            'isAdmin': isAdmin,
            'updateForm': updateForm,
            'participants': participants,
            'departmentData' : departmentData,
            'semesterData': semesterData,
            'userTypeData':userTypeData,
        })
    else:
       return render(request, 'events/view_event.html', {
            'event': event,
            'isAdmin': isAdmin,
        })


def registerAtEvent(request, event_id):

    event = get_object_or_404(Event, pk=event_id)

    event.participants.add(request.user)

    return redirect('events:viewEvent', event_id)