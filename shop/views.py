from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from shop.serializers import ProductSerializer 
from .models import Product

class ProductAPIListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderAPIListView(ListAPIView):
    # your code here
    ...

class OrderAPIRetriveView:
    # your code here
    ...


def order_api(request):
    # your order api code here
    ...



    