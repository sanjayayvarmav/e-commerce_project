from django.shortcuts import render

# Create your views here.
from shopapp.models import Product
from django.db.models import Q

def SearchProduct(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html', {'query':query,'product':product})
