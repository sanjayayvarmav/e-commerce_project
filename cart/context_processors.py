from django.core.exceptions import ObjectDoesNotExist

from.models import Cart_Id,CartItems
from.views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:

            cart=Cart_Id.objects.filter(cart_id=_cart_id(request))
   #         cart_items=CartItems.objects.all().filter(cart=cart[:1])
            cart_items=CartItems.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except ObjectDoesNotExist:
            item_count=0
    return {'item_count':item_count}
