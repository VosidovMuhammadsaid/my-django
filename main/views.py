from django.shortcuts import render
from .models import Banner,Category,Brand,Product,ProductAttribute
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

# Home Page
def index(request):
    banners=Banner.objects.all().order_by('-id')
    data=Product.objects.filter(is_featured=True).order_by('-id')
    context={ 
        'data':data,
        'banners':banners,
    }
    return render(request, 'main/index.html',context)

# Category
def category_list(request):
    data=Category.objects.all().order_by('-id')
    context={
        'data':data,
    }
    return render(request,'main/categories.html',context)
    
def brand_list(request):
    data=Brand.objects.all().order_by('-id')
    context={
        'data':data,
    }
    return render(request,'main/brand_list.html',context)


def product_list(request):
    data=Product.objects.all().order_by('-id')
    

    context={
        'data':data,
    }
    return render(request,'main/product_list.html',context)

# Product List According to Category

def category_product_list(request,cat_id):
    category=Category.objects.get(id=cat_id)
    data=Product.objects.filter(category=category).order_by('-id')

    context={
        'data':data,
    }
    return render(request,'main/category_product_list.html',context)



def brand_product_list(request,brand_id):
    brand=Brand.objects.get(id=brand_id)
    data=Product.objects.filter(brand=brand).order_by('-id')

    context={
        'data':data,
    }
    return render(request,'main/category_product_list.html',context)

def product_detail(request,slug,id):
    product=Product.objects.get(id=id) 
    related_products=Product.objects.filter(category=product.category).exclude(id=id)[:4]
    context={
        'data':product,
        'related_products':related_products,
    }
    return render(request,'main/product_detail.html',context)

def search(request):
    q=request.GET['q']
    data=Product.objects.filter(title__icontains=q).order_by('-id')
    
    context={
        'data':data,
    }
    return render(request,'main/search.html',context)

def filter_data(request):
    colors=request.GET.getlist('color[]')
    categories=request.GET.getlist('color[]')
    brands=request.GET.getlist('color[]')
    sizes=request.GET.getlist('color[]')
    allProducts=Product.objects.all().order_by('-id')
    t=render_to_string('ajax/product-list',{'data':allProducts})
    return JsonResponse({'data':t})