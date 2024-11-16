from django.shortcuts import render

# Create your views here.

from .models import Products
from .forms import ProductForms

def products_database_view(request):
    obj = Products.objects.get(productNumber=1)
    # context = {
    #     'category': obj.category,
    #     'title' : obj.title,
    #     'description': obj.description,
    #     'price': obj.price
    # }
    context = {
        'object': obj
    }
    return render (request, 'products/detail.html', context)

def product_create_view(request):
    form = ProductForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForms()
    context = {
        'form' : form
    }
    return render (request, product_create_view, context)