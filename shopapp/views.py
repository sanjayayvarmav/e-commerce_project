from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.
from shopapp.models import Category, Product



def allprodcat(request,c_slug=None):
    c_page=None
    allproducts=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        allproducts=Product.objects.all().filter(category=c_page,available=True)
    else:
        allproducts=Product.objects.all().filter(available=True)
    paginator = Paginator(allproducts,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products= paginator.page(paginator.num_pages)

    return render(request,'category.html',{'c_page':c_page,'products':products})


def p_details(request,c_slug,p_slug):
    try:
        products=Product.objects.get(category__slug=c_slug,slug=p_slug)
    except  Exception as e:
        raise e
    return render(request,'product.html',{'products':products})

