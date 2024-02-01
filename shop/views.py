from django.shortcuts import render
from rest_framework.generics import views
from shop.serializers import ProductSerializer 
from .models import Product

class ProductAPIListView(views.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer