from django.db import models
from core.models import BaseModel




class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
 


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(
        "Address", related_name="orders", on_delete=models.CASCADE
    )
    ordered_products = models.ManyToManyField(Product)


class Address(models.Model):
    customer_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
