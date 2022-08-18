from django.db import models

from shopapp.models import Product

class Cart_Id(models.Model):
    cart_id=models.CharField(max_length=100,blank=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['date_added']
    def __str__(self):
        return self.cart_id

class CartItems(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart_Id,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='CartItems'
        ordering=['products',]

    def sub_total(self):
        return self.products.price * self.quantity


