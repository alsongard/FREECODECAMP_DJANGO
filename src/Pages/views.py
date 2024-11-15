from django.shortcuts import render
from django.http import *

# Create your views here.
def contact_view(request, *args, **kwargs):
    print(f"*args : {args} \n **kwargs: {kwargs}")
    print(request)
    print(request.user)
    # return HttpResponse("<h1>This is my contact Page</h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>This is my about view</h1>")
    return render(request, "about.html", {})

def service_view(request, *args, **kwargs):
    contact_dict = {
        "company_name": "Alson Software & CyberSec Institution",
        "location": "Mars City",
        "services" : ["Software Development", "Penetration Testing", "IoT", "Robotics"]
    }
    return render(request, "services.html", contact_dict)