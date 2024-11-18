from django.shortcuts import render
from django.http import *
# Create your views here.
def simple_form_view(request):
    print(request.GET)
    print(request.POST)
    # return HttpResponse("<h1>Welcome back sir </h1>") # use this to check if url and view is configured properly
    return render(request, 'formsPractise/simpleForms.html', {})