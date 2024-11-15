from django.shortcuts import render

# Create your views here.

from .models import Products

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