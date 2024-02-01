from rest_framework import serializers
from .models import Product, Order, Address 



class ProductSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Product
        fields = ['id', 'name', 'description', 'price']



class OderSerializer(serializers.ModelSerializer):
    # complete this
    # no right answer, make it work 
    ...