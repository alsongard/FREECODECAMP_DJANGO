from django.shortcuts import render
from django.http import *
# Create your views here.
def contact_view(request, *args, **kwargs):
    print(f"*args : {args} \n **kwargs: {kwargs}")
    print(request)
    print(request.user)
    return HttpResponse("<h1>This is my contact Page</h1>")


def about_view(*args, **kwargs):
    return HttpResponse("<h1>This is my about view</h1>")
