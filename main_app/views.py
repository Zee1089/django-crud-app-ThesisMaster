# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>All of your Selected Research Articles Found Here</h1>')

# main_app/views.py

def about(request):
    return render(request, 'about.html')
