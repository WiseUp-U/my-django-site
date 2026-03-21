from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, "products/product_list.html", {'products' : products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/product_detail.html", {'product' : product })


from django.http import HttpResponse
import os
from django.conf import settings

def check_media(request):
    result = []

    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        for name in files:
            result.append(os.path.join(root, name))

    return HttpResponse(str(result))