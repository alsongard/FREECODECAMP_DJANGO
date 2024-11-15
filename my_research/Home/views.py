from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to Zetech University</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    contactdict = {
        "univesity_name": "Zetech University",
        "phone_number": "254714588863",
        'campus_names': ["Zetech Mangu Campus", "Zetech Ruiru Campus", "Zetech Nairobi Campus"],
        'location': ["Mangu", "Ruiru", "CBD"]
    }
    return render(request, "contact.html", contactdict)


"""



"""