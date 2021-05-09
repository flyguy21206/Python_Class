from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def index(request):
    response = {
    "Name" : "Richard Harrison", 

    "Track" : "Backend(Python)",

    "Message" : "Hello Mentor, I am always surprised when it works!"
    }

    return JsonResponse(response)
