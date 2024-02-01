from django.shortcuts import render
from rest_framework.generics import ListAPIView
from shop.serializers import ProductSerializer 
from .models import Product

class ProductAPIListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer