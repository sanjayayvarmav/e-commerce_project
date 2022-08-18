from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from shopapp.models import Product
from.models import Cart_Id,CartItems
from django.core.exceptions import ObjectDoesNotExist



def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart = Cart_Id.objects.get(cart_id=_cart_id(request))
    except ObjectDoesNotExist:
        cart = Cart_Id.objects.create(cart_id=_cart_id(request))
    cart.save()
    try:
        cart_item = CartItems.objects.get(products=product,cart=cart)
        if cart_item.quantity < cart_item.products.stock:
            cart_item.quantity += 1

    except ObjectDoesNotExist:
        cart_item=CartItems.objects.create(products=product,cart=cart,quantity=1)
    cart_item.save()
    return redirect('cart:cart_details')
def cart_details(request,total=0,counter=0,cart_items=None):
    try:
        cart = Cart_Id.objects.get(cart_id=_cart_id(request))
        cart_items=CartItems.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total += cart_item.products.price*cart_item.quantity
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))
def remove_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    cart=Cart_Id.objects.get(cart_id=_cart_id(request))
    cart_item=CartItems.objects.get(cart=cart,products=product)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:cart_details')

def delete_cart(request,product_id):
    cart=Cart_Id.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItems.objects.get(products=product,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_details')




