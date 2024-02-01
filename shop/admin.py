from django.contrib import admin
from .models import Product, Order, Address
from django.utils.text import Truncator



admin.AdminSite.site_header = "Shop Administration"
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','short_desc', 'price', 'is_deleted']
    list_filter = ['price']


    def short_desc(self, obj):
        length = 100
        return Truncator(obj.description).chars(length)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_date','list_products','shipping_address', 'is_deleted']
    list_filter = ['order_date']

    def list_products(self, obj):
        lop = [product.name for product in obj.ordered_products.all()] 
        return lop if len(lop) < 3 else ", ".join(lop[:2]) + " and {} more".format(len(lop) - 2)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'address_line_1', 'city', 'state', 'zip_code']
    list_display_links = ['customer_name', 'address_line_1']
    list_max_show_all = 50 