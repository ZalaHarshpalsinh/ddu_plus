
from django.shortcuts import render

# Create your views here.
def landingPage(request):
    return render(request, 'landing_page.html')