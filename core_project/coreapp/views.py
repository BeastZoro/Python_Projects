# views.py

from django.shortcuts import render, get_object_or_404
from .models import Products, Category

def index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    allproducts = Products.objects.all()
    return render(request, 'pages/index.html', {'products': products, 'categories': categories, 'allproducts': allproducts})

def products_category(request, cate_id):
    if cate_id == 0:
        category = 'All'
    else:
        category = get_object_or_404(Category, pk=cate_id)

    categories = Category.objects.all()
    products = Products.objects.filter(categories=category)
    allproducts = Products.objects.all()  # Retrieve all products

    return render(request, 'pages/index.html', {'products': products, 'category': category, 'categories': categories, 'allproducts': allproducts})

def hot_items(request):
    allproducts = Products.objects.all()
    return render(request, 'components/hot_items.html', {'allproducts': allproducts})
